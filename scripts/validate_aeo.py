#!/usr/bin/env python3
"""Validate source metadata and built output. Human review still verifies claim support."""
import argparse
from collections import Counter
import gzip
from pathlib import Path
import re
import sys
from urllib.parse import urljoin
import xml.etree.ElementTree as ET

import yaml
from validate_site import BASE, Document

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from hooks.metadata import page_type


class Metadata(Document):
    def __init__(self, html):
        self.meta = {}
        self.canonicals = []
        self.text = []
        self.headings = []
        self.heading = None
        super().__init__(html)

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "meta":
            key = values.get("name", values.get("property"))
            self.meta.setdefault(key, []).append(values.get("content", ""))
        if tag == "link" and values.get("rel") == "canonical":
            self.canonicals.append(values.get("href"))
        if tag == "h1":
            self.heading = ""
        if tag == "br" and self.heading is not None:
            self.heading += " "
        super().handle_starttag(tag, attrs)

    def handle_data(self, data):
        if self.heading is not None:
            self.heading += data
        if self.script is None:
            self.text.append(data)
        super().handle_data(data)

    def handle_endtag(self, tag):
        if tag == "h1" and self.heading is not None:
            self.headings.append(self.heading.strip().rstrip("¶").strip())
            self.heading = None
        super().handle_endtag(tag)


def source_data(source):
    text = source.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        _, front, body = re.split(r"^---\s*$", text, maxsplit=2, flags=re.M)
        return yaml.safe_load(front) or {}, body
    return {}, text


def summary_errors(body, article):
    """Require an actual introductory paragraph, not metadata or a link list.

    Existing What It Is definitions qualify. Claims with external citations must
    retain a visible source/evidence section; semantic entailment is human-only.
    """
    if not article:
        return []
    opening = re.split(r"^## (?:Why|Best|Required|Examples|Quality|When|How)", body, maxsplit=1, flags=re.M)[0]
    paragraphs = re.split(r"\n\s*\n", opening)
    prose = [p for p in paragraphs if not p.lstrip().startswith(("#", "**Stage", "**Score", "**Evidence", "|", "-", "<"))]
    errors = []
    if not any(len(re.findall(r"\b[\w'-]+\b", p)) >= 10 for p in prose):
        errors.append("missing answer-first summary/definition (10+ words before detail sections)")
    # External evidence remains visible, never inferred from a schema label.
    if re.search(r"^##+ .*?(?:Sources|References|Evidence)", body, re.M | re.I):
        section = re.split(r"^##+ .*?(?:Sources|References|Evidence).*?$", body, flags=re.M | re.I)[-1]
        if not re.search(r"https?://", body) and not re.search(r"observation|internal|practitioner", section, re.I):
            errors.append("source/evidence section lacks a citation or explicit observational basis")
    return errors


def audit_aeo(site, source_root=None):
    source_root = source_root or ROOT / "docs"
    errors, descriptions, expected_urls = [], {}, set()
    counts = Counter()
    for source in sorted(source_root.rglob("*.md")):
        rel = source.relative_to(source_root)
        if "overrides" in rel.parts:
            continue
        label = rel.as_posix()
        meta, body = source_data(source)
        description = meta.get("description")
        if not isinstance(description, str) or not description.strip():
            errors.append(f"{label}: missing explicit page description")
            description = ""
        normalized = " ".join(description.casefold().split())
        if normalized and normalized in descriptions:
            errors.append(f"{label}: duplicate description with {descriptions[normalized]}")
        descriptions[normalized] = label
        route = rel.parent.as_posix() + "/" if rel.name == "index.md" else rel.with_suffix("").as_posix() + "/"
        if route == "./":
            route = ""
        url = urljoin(BASE, route)
        expected_urls.add(url)
        path = site / route / "index.html"
        if not path.exists():
            errors.append(f"{label}: missing built page")
            continue
        try:
            doc = Metadata(path.read_text(encoding="utf-8"))
        except (ValueError, TypeError) as exc:
            errors.append(f"{label}: invalid JSON-LD: {exc}")
            continue
        kind = page_type(label)
        counts[kind] += 1
        errors.extend(f"{label}: {e}" for e in summary_errors(body, kind == "Article"))
        for key in ("description", "og:description", "twitter:description"):
            if doc.meta.get(key) != [description]:
                errors.append(f"{label}: {key} must occur once and match source description")
        if doc.canonicals != [url] or doc.meta.get("og:url") != [url]:
            errors.append(f"{label}: canonical/OG URL mismatch")
        if doc.meta.get("og:type") != ["article" if kind == "Article" else "website"]:
            errors.append(f"{label}: OG type mismatch")
        if len(doc.schemas) != 1:
            errors.append(f"{label}: expected one JSON-LD graph")
            continue
        graph = doc.schemas[0].get("@graph", [])
        expected_types = Counter(["Organization", "WebSite", "BreadcrumbList", "CollectionPage" if kind == "CollectionPage" else "WebPage"] + (["Article"] if kind == "Article" else []))
        if label == "index.md":
            del expected_types["BreadcrumbList"]
        if Counter(item.get("@type") for item in graph) != expected_types:
            errors.append(f"{label}: inappropriate JSON-LD types")
        ids = [item.get("@id") for item in graph]
        if len(ids) != len(set(ids)) or None in ids:
            errors.append(f"{label}: missing/duplicate entity IDs")
        def references(value):
            if isinstance(value, dict):
                if set(value) == {"@id"} and value["@id"] not in ids:
                    errors.append(f"{label}: unresolved graph reference {value['@id']}")
                for child in value.values():
                    references(child)
            elif isinstance(value, list):
                for child in value:
                    references(child)
        references(graph)
        for item in graph:
            typ = item.get("@type")
            if any(k in item for k in ("datePublished", "dateReviewed", "reviewedBy")):
                errors.append(f"{label}: unverified date/reviewer metadata")
            if "dateModified" in item and typ != "Article":
                errors.append(f"{label}: dateModified belongs only to Article")
            if typ in ("WebPage", "CollectionPage", "Article"):
                suffix = "#article" if typ == "Article" else "#webpage"
                if item.get("url") != url or item.get("@id") != url + suffix or item.get("description") != description:
                    errors.append(f"{label}: structured identity/description parity failure")
                title = " ".join(doc.headings[0].split()) if doc.headings else ""
                if not title:
                    errors.append(f"{label}: missing visible H1")
                if title and item.get("headline", item.get("name")) != title:
                    errors.append(f"{label}: schema title differs from source H1")
                if typ == "Article" and item.get("mainEntityOfPage") != {"@id": url + "#webpage"}:
                    errors.append(f"{label}: Article not linked to canonical WebPage")
            if typ == "Organization" and item.get("@id") != "https://riggg.com/#organization":
                errors.append(f"{label}: unstable organization identity")
            if typ == "WebSite" and item.get("@id") != BASE + "#website":
                errors.append(f"{label}: unstable website identity")
    sitemap = site / "sitemap.xml"
    if not sitemap.exists():
        errors.append("missing sitemap.xml")
    else:
        try:
            xml = ET.fromstring(sitemap.read_bytes())
            ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            urls = [e.text for e in xml.findall("s:url/s:loc", ns)]
            if set(urls) != expected_urls or len(urls) != len(expected_urls):
                errors.append("sitemap differs from published canonical page set")
            if xml.findall("s:url/s:lastmod", ns):
                errors.append("sitemap contains unverified lastmod dates")
            compressed = site / "sitemap.xml.gz"
            if compressed.exists() and gzip.decompress(compressed.read_bytes()) != sitemap.read_bytes():
                errors.append("compressed sitemap differs from sitemap.xml")
        except (ET.ParseError, OSError) as exc:
            errors.append(f"invalid sitemap: {exc}")
    robots = site / "robots.txt"
    if not robots.exists() or "Sitemap: " + BASE + "sitemap.xml" not in robots.read_text():
        errors.append("robots.txt missing canonical sitemap")
    return counts, errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", nargs="?", type=Path, default=Path("site"))
    args = parser.parse_args()
    counts, errors = audit_aeo(args.site)
    print(f"AEO: {sum(counts.values())} pages; {dict(counts)}; {len(errors)} errors.")
    print("\n".join(errors))
    raise SystemExit(bool(errors))
