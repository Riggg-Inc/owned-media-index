"""Conservative page identity; no inferred publication or review dates."""
from pathlib import Path, PurePosixPath
from html import unescape
import re


def page_type(source):
    path = PurePosixPath(source)
    if path.name == "index.md":
        return "CollectionPage"
    if path.parts[0] in ("patterns", "tools"):
        return "Article"
    return "WebPage"


def build_schema(page, config, breadcrumbs, freshness=None):
    base = config["site_url"].rstrip("/") + "/"
    canonical = page.canonical_url
    organization = "https://riggg.com/#organization"
    website = base + "#website"
    kind = page_type(page.file.src_uri)
    heading = re.search(r"<h1[^>]*>(.*?)</h1>", page.content or "", re.S)
    title = unescape(re.sub(r"<[^>]+>", "", re.sub(r'<a class="headerlink".*?</a>', "", heading.group(1)))).strip() if heading else page.title
    if page.file.src_uri == "index.md":
        title = "Owned Media Index"
    identity = canonical + "#webpage"
    entity = {
        "@type": "WebPage" if kind == "Article" else kind,
        "@id": identity, "url": canonical, "name": title,
        "description": page.meta.get("description", ""),
        "isPartOf": {"@id": website},
        "breadcrumb": {"@id": canonical + "#breadcrumb"},
    }
    graph = [
        {"@type": "Organization", "@id": organization, "name": "Riggg Inc.",
         "url": "https://riggg.com", "logo": base + "assets/riggg-logo-white.png"},
        {"@type": "WebSite", "@id": website, "url": base,
         "name": config["site_name"], "description": config["site_description"],
         "publisher": {"@id": organization}},
        entity,
        dict(breadcrumbs, **{"@id": canonical + "#breadcrumb"}),
    ]
    if page.file.src_uri == "index.md":
        entity.pop("breadcrumb")
        graph = [item for item in graph if item.get("@type") != "BreadcrumbList"]
    if kind == "Article":
        entity["mainEntity"] = {"@id": canonical + "#article"}
        graph.append({"@type": "Article", "@id": canonical + "#article",
                      "url": canonical, "headline": title,
                      "description": page.meta.get("description", ""),
                      "mainEntityOfPage": {"@id": identity},
                      "publisher": {"@id": organization}})
    revision = (freshness or {}).get("revision", {})
    if revision.get("state") == "committed":
        for item in graph:
            if item.get("@type") in ("Article", "WebPage", "CollectionPage"):
                item["dateModified"] = revision["timestamp"]
    return {"@context": "https://schema.org", "@graph": graph}


def on_page_context(context, page, config, nav):
    # Lazy import: fact_checks imports page_type from this module.
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from hooks.freshness import page_freshness
    context["page_kind"] = page_type(page.file.src_uri)
    root = Path(config["config_file_path"]).resolve().parent
    freshness = page_freshness(root, page.file.src_uri)
    context["page_freshness"] = freshness
    context["page_schema"] = build_schema(page, config, context["breadcrumb_schema"], freshness)
    return context
