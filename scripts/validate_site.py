#!/usr/bin/env python3
"""Audit built HTML links and breadcrumb parity using only the Python stdlib."""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

BASE = "https://index.riggg.com/"

class Document(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.breadcrumbs, self.schemas = set(), [], [], []
        self.in_nav = False
        self.nav_count = 0
        self.current = None
        self.script = None
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag in ("a", "link", "img", "script", "source"):
            url = attrs.get("href") if tag in ("a", "link") else attrs.get("src")
            if url:
                self.links.append(url)
        if tag == "nav" and attrs.get("aria-label") == "Breadcrumb":
            self.in_nav = True
            self.nav_count += 1
        if self.in_nav and tag in ("a", "span") and "aria-hidden" not in attrs:
            self.current = {"name": "", "href": attrs.get("href"), "current": attrs.get("aria-current")}
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.script = ""

    def handle_data(self, data):
        if self.current is not None:
            self.current["name"] += data
        if self.script is not None:
            self.script += data

    def handle_endtag(self, tag):
        if tag in ("a", "span") and self.current is not None:
            self.current["name"] = self.current["name"].strip()
            self.breadcrumbs.append(self.current)
            self.current = None
        if tag == "nav":
            self.in_nav = False
        if tag == "script" and self.script is not None:
            self.schemas.append(json.loads(self.script))
            self.script = None


def audit(site, breadcrumbs=True):
    docs, errors = {}, []
    for path in sorted(site.rglob("*.html")):
        rel = path.relative_to(site).as_posix()
        url = urljoin(BASE, rel.removesuffix("index.html"))
        try:
            docs[url] = (path, Document(path.read_text()))
        except ValueError as exc:
            errors.append(f"{rel}: invalid JSON-LD: {exc}")
    links = 0
    for url, (path, doc) in docs.items():
        for href in doc.links:
            target = urlsplit(urljoin(url, href))
            if target.netloc != urlsplit(BASE).netloc or target.scheme not in ("http", "https"):
                continue
            links += 1
            dest = site / unquote(target.path).lstrip("/")
            if dest.is_dir():
                dest /= "index.html"
            if not dest.is_file():
                errors.append(f"{path.relative_to(site)}: missing target {href}")
            elif target.fragment and dest.suffix == ".html":
                parsed = next((d for p, d in docs.values() if p == dest), None)
                if parsed and unquote(target.fragment) not in parsed.ids:
                    errors.append(f"{path.relative_to(site)}: missing fragment {href}")
        if not breadcrumbs:
            continue
        if doc.nav_count != 1 or not doc.breadcrumbs:
            errors.append(f"{path.relative_to(site)}: expected one breadcrumb navigation")
            continue
        crumbs = doc.breadcrumbs
        if crumbs[0]["name"] != "Home" or crumbs[-1]["current"] != "page":
            errors.append(f"{path.relative_to(site)}: invalid home/current breadcrumb")
        if any(c["current"] for c in crumbs[:-1]) or crumbs[-1]["href"]:
            errors.append(f"{path.relative_to(site)}: current page must be the final non-link")
        graphs = [item for schema in doc.schemas for item in schema.get("@graph", [schema])]
        lists = [item for item in graphs if item.get("@type") == "BreadcrumbList"]
        expected = [{"@type": "ListItem", "position": i, "name": c["name"], "item": urljoin(url, c["href"]) if c["href"] else url} for i, c in enumerate(crumbs, 1)]
        # The not-found page has navigation but is not a canonical content page.
        if path.name != "404.html" and (len(lists) != 1 or lists[0].get("itemListElement") != expected):
            errors.append(f"{path.relative_to(site)}: BreadcrumbList differs from visible trail")
    return docs, links, errors

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", nargs="?", type=Path, default=Path("site"))
    parser.add_argument("--links-only", action="store_true")
    args = parser.parse_args()
    docs, links, errors = audit(args.site, not args.links_only)
    print(f"Audited {len(docs)} HTML pages and {links} internal link/resource references; {len(errors)} errors.")
    print("\n".join(errors))
    raise SystemExit(bool(errors))
