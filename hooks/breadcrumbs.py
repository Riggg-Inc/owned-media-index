"""Build trails from published directory indexes, not the deliberately sparse nav.

Missing directory indexes are skipped: breadcrumbs must never invent pages or
promote repository drafts into the documentation build.
"""
from pathlib import PurePosixPath


def build_trail(page, files):
    pages = {file.src_uri: file.page for file in files.documentation_pages() if file.page}
    trail = []
    home = pages.get("index.md")
    if home:
        trail.append({"name": "Home", "url": home.url, "canonical": home.canonical_url})
    source = PurePosixPath(page.file.src_uri)
    for directory in reversed(source.parent.parents):
        # PurePosixPath.parents includes '.', handled by Home above.
        if str(directory) != ".":
            ancestor = pages.get(str(directory / "index.md"))
            if ancestor and ancestor is not page:
                trail.append({"name": ancestor.title, "url": ancestor.url, "canonical": ancestor.canonical_url})
    if str(source.parent) != ".":
        ancestor = pages.get(str(source.parent / "index.md"))
        if ancestor and ancestor is not page:
            trail.append({"name": ancestor.title, "url": ancestor.url, "canonical": ancestor.canonical_url})
    if page is not home:
        trail.append({"name": page.title, "url": page.url, "canonical": page.canonical_url})
    return trail


def on_nav(nav, config, files):
    global published_files
    published_files = files
    return nav


def on_page_context(context, page, config, nav):
    # All pages have been populated by the rendering stage, including off-nav pages.
    trail = build_trail(page, published_files)
    context["breadcrumbs"] = trail
    context["breadcrumb_schema"] = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "name": crumb["name"], "item": crumb["canonical"]}
            for i, crumb in enumerate(trail, 1)
        ],
    }
    return context
