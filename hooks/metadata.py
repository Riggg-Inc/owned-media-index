"""Conservative page identity; no inferred publication or review dates."""
from pathlib import PurePosixPath
from html import unescape
import re


def page_type(source):
    path = PurePosixPath(source)
    if path.name == "index.md":
        return "CollectionPage"
    if path.parts[0] in ("patterns", "tools"):
        return "Article"
    return "WebPage"


def build_schema(page, config, breadcrumbs):
    base = config["site_url"].rstrip("/") + "/"
    canonical = page.canonical_url
    organization = "https://riggg.com/#organization"
    website = base + "#website"
    kind = page_type(page.file.src_uri)
    heading = re.search(r"<h1[^>]*>(.*?)</h1>", page.content or "", re.S)
    title = unescape(re.sub(r"<[^>]+>", "", re.sub(r'<a class="headerlink".*?</a>', "", heading.group(1)))).strip() if heading else page.title
    if page.file.src_uri == "index.md":
        title = "The Open Standard for Owned Media"
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
    if kind == "Article":
        entity["mainEntity"] = {"@id": canonical + "#article"}
        graph.append({"@type": "Article", "@id": canonical + "#article",
                      "url": canonical, "headline": title,
                      "description": page.meta.get("description", ""),
                      "mainEntityOfPage": {"@id": identity},
                      "publisher": {"@id": organization}})
    return {"@context": "https://schema.org", "@graph": graph}


def on_page_context(context, page, config, nav):
    context["page_schema"] = build_schema(page, config, context["breadcrumb_schema"])
    context["page_kind"] = page_type(page.file.src_uri)
    return context
