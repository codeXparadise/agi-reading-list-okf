#!/usr/bin/env python3
"""Generate the retrieval layer for the bundle: semantic section chunks and page chunks.

Reads the canonical documents in papers/*.md (which stay untouched and authoritative)
and writes, deterministically:

    paper-sections/<paper-slug>/index.md + <NN>-<section>.md
    paper-pages/<paper-slug>/index.md + page-<NNN>.md

Sections come from the paper's own headings, in document order, with headings that are
not real sections (titles, author lines, figure labels, stray math) rejected and their
text merged into the preceding chunk. Papers whose frontmatter says
`extraction.full_text: external-only` get a section index that says so and no page chunks.

Usage:
    python tools/build_chunks.py .          # regenerate everything
    python tools/build_chunks.py . --check  # report what would change, write nothing
"""
import os, re, sys, shutil, unicodedata

GENERATED_AT = "2026-11-17T16:30:00Z"
GENERATOR = "tools/build_chunks.py"
WRITTEN = set()

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
PAGE_RE = re.compile(r"^<!-- page (\d+) -->\s*$", re.M)
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")

ROLE_PATTERNS = [
    ("abstract", r"^(abstract|summary)\b"),
    ("introduction", r"^(introduction|motivation)\b"),
    ("background", r"^(related work|background|previous work|prior work|literature)\b"),
    ("method", r"^(method|methods|methodology|model|models|approach|architecture|algorithm|framework|the \w+ (library|model)|adversarial nets|neural networks for)\b"),
    ("experiments", r"^(experiments?|experimental|evaluation|setup|implementation|training)\b"),
    ("results", r"^(results?|analysis|discussions?|ablation|why )\b"),
    ("limitations", r"^(limitations?|threats to validity)\b"),
    ("conclusion", r"^(conclusions?|future work|concluding)\b"),
    ("references", r"^(references|bibliography)\b"),
    ("appendix", r"^(appendix|supplementary|appendices)\b"),
]
BAD_CHARS = "=⇠←→≠≈∑√∈∀∃λθαβγδμσΔΘ−·±≤≥∞∂∫"
STOP_HEADS = {"contents", "abstract", "preface"}


def frontmatter(text):
    m = FM_RE.match(text)
    return (m.group(1) if m else ""), (text[m.end():] if m else text)


def fm_get(fm, key):
    m = re.search(r"^%s:\s*(.+)$" % re.escape(key), fm, re.M)
    return m.group(1).strip().strip('"') if m else None


def fm_list(fm, key):
    raw = fm_get(fm, key)
    if not raw:
        return []
    return [x.strip().strip('"').strip("'") for x in raw.strip("[]").split(",") if x.strip()]


def slugify(s, limit=52):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"^[\d]+(\.[\d]+)*\.?\s+", "", s)   # drop leading section numbering
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:limit].strip("-") or "section"


def role_of(heading):
    low = heading.strip().lower()
    low = re.sub(r"^\d+(\.\d+)*\.?\s+", "", low)
    for role, pat in ROLE_PATTERNS:
        if re.search(pat, low):
            return role
    return "other"


def is_real_heading(h, paper_title):
    t = h.strip()
    if not t or len(t) < 4 or len(t) > 80:
        return False
    if any(c in t for c in BAD_CHARS):
        return False
    if "@" in t or "∗" in t or "†" in t:
        return False
    if t.rstrip(".").lower() in STOP_HEADS:
        return t.strip().lower() == "abstract"      # keep a real Abstract heading
    if re.sub(r"[^a-z0-9]+", " ", t.lower()).strip() == re.sub(r"[^a-z0-9]+", " ", paper_title.lower()).strip():
        return False
    words = t.split()
    if len(words) > 12:
        return False
    if len(words) == 1 and len(t) < 6:
        return False
    if t.endswith(",") or ",!" in t:
        return False
    if re.match(r"^\d+(\.\d+)*\.?\s+\S", t):
        return True
    low = t.lower()
    for _, pat in ROLE_PATTERNS:
        if re.search(pat, re.sub(r"^\d+(\.\d+)*\.?\s+", "", low)):
            return True
    letters = [c for c in t if c.isalpha()]
    if not letters or t.endswith("."):
        return False
    upper_ratio = sum(c.isupper() for c in letters) / len(letters)
    title_ratio = sum(1 for w in words if w[:1].isupper()) / len(words)
    return upper_ratio > 0.7 or title_ratio >= 0.75


def clean_snippet(text, limit=150):
    t = IMG_RE.sub(" ", text)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"\\", "", t)
    t = re.sub(r"[#>*_`]", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    if len(t) > limit:
        t = t[:limit].rsplit(" ", 1)[0] + "…"
    return t.replace('"', "'") or "(no text on this page)"


def rel_topic(link):
    """Bundle-absolute topic path -> relative from paper-sections/<slug>/ or paper-pages/<slug>/."""
    return "../.." + link if link.startswith("/") else link


def rel_asset(link):
    """Turn a bundle-absolute asset link into a path relative to paper-*/<slug>/."""
    if link.startswith("/"):
        return "../.." + link
    return link


def to_relative(text, paper_rel):
    """Rewrite bundle-absolute links (assets) as relative ones, and point paper links at the canonical doc."""
    text = IMG_RE.sub(lambda m: m.group(0).replace(m.group(1), rel_asset(m.group(1))), text)
    return text


# --------------------------------------------------------------------------- parsing
def parse_paper(path):
    text = open(path, encoding="utf-8").read()
    fm, body = frontmatter(text)
    title = fm_get(fm, "title") or ""
    seq = int(fm_get(fm, "sequence") or 0)
    topics = fm_list(fm, "topics")
    full = fm_get(fm, "full_text")
    if not full:
        m = re.search(r"^  full_text:\s*(\S+)$", fm, re.M)
        full = m.group(1) if m else "external-only"
    m = re.search(r"^## Full text\n(.*?)^## Relationships\n", body, re.S | re.M)
    return {
        "path": path,
        "title": title,
        "sequence": seq,
        "topics": topics,
        "external_only": full.strip() == "external-only",
        "fulltext": m.group(1) if m else "",
    }


def split_sections(fulltext, title):
    """Return [(heading, role, text, pages)] in document order, using the paper's own headings."""
    lines = fulltext.split("\n")
    chunks, cur = [], {"heading": None, "text": [], "pages": set()}
    page = 1
    for line in lines:
        pm = PAGE_RE.match(line.strip()) if line.strip().startswith("<!-- page") else None
        if pm:
            page = int(pm.group(1))
            cur["pages"].add(page)
            continue
        hm = re.match(r"^(#{2,3})\s+(.*)$", line)
        if hm and is_real_heading(hm.group(2), title):
            chunks.append(cur)
            cur = {"heading": hm.group(2).strip(), "text": [], "pages": {page}}
            continue
        cur["text"].append(line)
        if line.strip():
            cur["pages"].add(page)
    chunks.append(cur)

    out, seen = [], set()
    for c in chunks:
        body = "\n".join(c["text"]).strip()
        body = re.sub(r"\n{3,}", "\n\n", body)
        if not body and c["heading"] is None:
            continue
        # A heading with no prose under it is a table-of-contents entry, an author line
        # or a figure label that slipped through the heading filter. Drop it rather than
        # invent a section: the real section, if any, appears later with its own text.
        if c["heading"] is not None and len(body.split()) < 12:
            continue
        # Table-of-contents lines survive extraction as "Section name 12"; they carry the
        # page number in the heading and only a line or two of body text.
        if c["heading"] is not None and re.search(r"\s\d{1,3}$", c["heading"]) and len(body.split()) < 40:
            continue
        heading = c["heading"] or "Front matter"
        role = role_of(heading) if c["heading"] else "front-matter"
        if role == "abstract" and not re.search(r"^\s*(\d+\.?\s*)?abstract", heading.lower()):
            role = "other"
        base = slugify(heading) if c["heading"] else "front-matter"
        slug, i = base, 2
        while slug in seen:
            slug = "%s-%d" % (base, i); i += 1
        seen.add(slug)
        pages = sorted(p for p in c["pages"] if p)
        out.append({"heading": heading, "role": role, "slug": slug, "text": body, "pages": pages})
    if len(out) < 3:
        allpages = sorted({p for c in out for p in c["pages"]})
        whole = "\n\n".join(c["text"] for c in out if c["text"]).strip()
        return [{"heading": "Full text", "role": "other", "slug": "full-text", "text": whole, "pages": allpages}]
    return out


def split_pages(fulltext):
    """Return [(page_number, text)] preserving the original text of each page."""
    pages, cur, num = [], [], None
    for line in fulltext.split("\n"):
        s = line.strip()
        m = re.match(r"^<!-- page (\d+) -->$", s)
        if m:
            if num is not None:
                pages.append((num, "\n".join(cur).strip()))
            num = int(m.group(1)); cur = []
            continue
        cur.append(line)
    if num is not None:
        pages.append((num, "\n".join(cur).strip()))
    return [(n, re.sub(r"\n{3,}", "\n\n", t) or "_No extractable text on this page._") for n, t in pages]


# --------------------------------------------------------------------------- writers
def write(path, text, check, changed):
    written = WRITTEN
    written.add(os.path.normpath(path))
    old = None
    if os.path.exists(path):
        old = open(path, encoding="utf-8").read()
    if old == text:
        return
    changed.append(path)
    if not check:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").write(text)


def yaml_str(s):
    if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 _./&()'+-]*", s or "") and ": " not in (s or ""):
        return s
    return '"%s"' % (s or "").replace('\\', '\\\\').replace('"', '\\"')


def build(root, check=False):
    papers_dir = os.path.join(root, "papers")
    sec_dir = os.path.join(root, "paper-sections")
    page_dir = os.path.join(root, "paper-pages")
    changed, report = [], []

    papers = []
    for name in sorted(os.listdir(papers_dir)):
        if not name.endswith(".md") or name == "index.md":
            continue
        papers.append(parse_paper(os.path.join(papers_dir, name)))
    papers.sort(key=lambda p: p["sequence"])

    written = set()
    counts = {}

    for p in papers:
        slug = os.path.splitext(os.path.basename(p["path"]))[0]
        canonical = "../../papers/%s.md" % slug
        sec_out = os.path.join(sec_dir, slug)
        pg_out = os.path.join(page_dir, slug)

        sections = [] if p["external_only"] else split_sections(p["fulltext"], p["title"])
        pages = [] if p["external_only"] else split_pages(p["fulltext"])
        counts[slug] = (len(sections), len(pages))

        # ---------------- semantic sections
        if p["external_only"]:
            report.append((p["sequence"], p["title"], "external-only",
                           "no full text in the bundle: section index marks it summary/link-only, no page chunks"))
            idx = ["# %02d - %s - sections" % (p["sequence"], p["title"]), "",
                   "**Summary / link-only paper.** This item is a web article, book chapter or thesis that is not "
                   "distributed as an open PDF, so the bundle holds a summary and a canonical link instead of full "
                   "text. There are no semantic section chunks and no page chunks for it.",
                   "",
                   "* Canonical document: [%02d - %s](%s) - summary, metadata and relationships" % (p["sequence"], p["title"], canonical),
                   "* Read the original: %s" % (fm_get(frontmatter(open(p["path"], encoding="utf-8").read())[0], "resource") or ""),
                   ]
            write(os.path.join(sec_out, "index.md"), "\n".join(idx) + "\n", check, changed)
            write(os.path.join(pg_out, "index.md"),
                  "# %02d - %s - pages\n\n**Summary / link-only paper.** No page chunks exist for this item: the "
                  "bundle does not hold its full text, so no page-level evidence can be cited from it.\n\n"
                  "* Canonical document: [%02d - %s](%s)\n" % (p["sequence"], p["title"], p["sequence"], p["title"], canonical),
                  check, changed)
            continue

        # index of sections
        idx = ["# %02d - %s - sections" % (p["sequence"], p["title"]), "",
               "Semantic chunks for this paper, in the paper's own section order. Retrieve these first; drop to "
               "[page chunks](../../paper-pages/%s/index.md) only for exact quotations, equations, figures or citations." % slug,
               "",
               "* Canonical document: [%02d - %s](%s)" % (p["sequence"], p["title"], canonical),
               "", "## Sections", ""]
        for i, s in enumerate(sections, 1):
            idx.append("%d. [%s](%02d-%s.md) - `%s`%s · pages %s - %s" % (
                i, s["heading"], i, s["slug"], s["role"],
                (" · %d words" % len(s["text"].split())),
                (str(s["pages"][0]) if s["pages"] else "-"),
                (str(s["pages"][-1]) if s["pages"] else "-")))
        idx.append("")
        idx.append("## Pages")
        idx.append("")
        idx.append("* [%d page chunks](../../paper-pages/%s/index.md)" % (len(pages), slug))
        write(os.path.join(sec_out, "index.md"), "\n".join(idx) + "\n", check, changed)

        for i, s in enumerate(sections, 1):
            fm = ["---",
                  "type: Research Paper Chunk",
                  "chunk_type: semantic-section",
                  "paper: %s" % canonical,
                  "source: %s" % canonical,
                  "paper_title: %s" % yaml_str(p["title"]),
                  "sequence: %d" % p["sequence"],
                  "section: %s" % yaml_str(s["heading"]),
                  "section_role: %s" % s["role"],
                  "section_index: %d" % i,
                  "pages: [%s]" % ", ".join(str(x) for x in s["pages"]),
                  "topics: [%s]" % ", ".join('"%s"' % rel_topic(t) for t in p["topics"]),
                  "description: %s" % yaml_str(clean_snippet(s["text"])),
                  "status: stable",
                  "generated: { by: %s, at: %s }" % (GENERATOR, GENERATED_AT),
                  "---", ""]
            body = ["# %s" % s["heading"], "",
                    "> Section %d of %d from [%02d - %s](%s) · `%s` · pages %s" % (
                        i, len(sections), p["sequence"], p["title"], canonical, s["role"],
                        ("%d-%d" % (s["pages"][0], s["pages"][-1])) if s["pages"] else "n/a"),
                    ""]
            body.append(to_relative(s["text"], canonical))
            body.append("")
            body.append("---")
            body.append("")
            body.append("Full document: [%02d - %s](%s) · Page-level evidence: [paper-pages/%s](../../paper-pages/%s/index.md)" % (
                p["sequence"], p["title"], canonical, slug, slug))
            write(os.path.join(sec_out, "%02d-%s.md" % (i, s["slug"])), "\n".join(fm + body) + "\n", check, changed)

        # ---------------- page chunks
        idx = ["# %02d - %s - pages" % (p["sequence"], p["title"]), "",
               "Page-level evidence chunks, one per page of the source PDF, text preserved as extracted. Use these "
               "only when a question needs an exact quotation, equation, figure or citation; otherwise prefer the "
               "[semantic sections](../../paper-sections/%s/index.md)." % slug, "",
               "* Canonical document: [%02d - %s](%s)" % (p["sequence"], p["title"], canonical),
               "* Pages: %d" % len(pages), "", "## Pages", ""]
        for n, t in pages:
            idx.append("* [Page %03d](page-%03d.md) - %s" % (n, n, clean_snippet(t, 110)))
        write(os.path.join(pg_out, "index.md"), "\n".join(idx) + "\n", check, changed)

        for n, t in pages:
            fm = ["---",
                  "type: Research Paper Chunk",
                  "chunk_type: page",
                  "paper: %s" % canonical,
                  "source: %s" % canonical,
                  "paper_title: %s" % yaml_str(p["title"]),
                  "sequence: %d" % p["sequence"],
                  "page: %d" % n,
                  "pages: [%d]" % n,
                  "page_of: %d" % len(pages),
                  "topics: [%s]" % ", ".join('"%s"' % rel_topic(x) for x in p["topics"]),
                  "description: %s" % yaml_str(clean_snippet(t)),
                  "status: stable",
                  "generated: { by: %s, at: %s }" % (GENERATOR, GENERATED_AT),
                  "---", ""]
            body = ["# Page %d of %d - %s" % (n, len(pages), p["title"]), "",
                    "> Page %d of the source PDF, verbatim as extracted. Canonical document: [%02d - %s](%s)" % (
                        n, p["sequence"], p["title"], canonical),
                    ""]
            body.append(to_relative(t, canonical))
            body.append("")
            body.append("---")
            body.append("")
            prev_l = "[previous page](page-%03d.md)" % (n - 1) if n > 1 else "first page"
            next_l = "[next page](page-%03d.md)" % (n + 1) if n < len(pages) else "last page"
            body.append("%s · %s · [all pages](index.md)" % (prev_l, next_l))
            write(os.path.join(pg_out, "page-%03d.md" % n), "\n".join(fm + body) + "\n", check, changed)

        if len(sections) <= 2:
            report.append((p["sequence"], p["title"], "few-headings",
                           "only %d usable headings found; chunks are conservative rather than invented" % len(sections)))

    # ---------------- top-level indexes
    lines = ["# Paper sections", "",
             "Semantic chunks of every paper, split on the paper's own headings and kept in document order. This is "
             "the first retrieval layer: it is small enough to read a chunk whole, and it carries the paper, the "
             "section, the role and the page range in frontmatter.", "",
             "For exact quotations, equations, figures or citations, drop to [paper-pages](../paper-pages/index.md). "
             "The canonical, complete documents remain in [papers](../papers/index.md).", ""]
    for p in papers:
        slug = os.path.splitext(os.path.basename(p["path"]))[0]
        if p["external_only"]:
            lines.append("* [%02d - %s](%s/index.md) - summary / link-only, no full text in the bundle" % (p["sequence"], p["title"], slug))
        else:
            n_sec = counts.get(slug, (0, 0))[0]
            lines.append("* [%02d - %s](%s/index.md) - %d semantic sections" % (p["sequence"], p["title"], slug, n_sec))
    write(os.path.join(sec_dir, "index.md"), "\n".join(lines) + "\n", check, changed)

    lines = ["# Paper pages", "",
             "Page-level evidence chunks: one file per page of the source PDF, text preserved as extracted, with the "
             "page number in frontmatter and in the filename.", "",
             "Use these only when a question needs an exact quotation, an equation as printed, a figure or a precise "
             "citation. For everything else, prefer [paper-sections](../paper-sections/index.md).", ""]
    for p in papers:
        slug = os.path.splitext(os.path.basename(p["path"]))[0]
        if p["external_only"]:
            lines.append("* [%02d - %s](%s/index.md) - summary / link-only, no page chunks" % (p["sequence"], p["title"], slug))
        else:
            n_pg = counts.get(slug, (0, 0))[1]
            lines.append("* [%02d - %s](%s/index.md) - %d pages" % (p["sequence"], p["title"], slug, n_pg))
    write(os.path.join(page_dir, "index.md"), "\n".join(lines) + "\n", check, changed)

    # ---------------- prune anything the generator no longer produces
    for base in (sec_dir, page_dir):
        for dirpath, dirnames, filenames in os.walk(base):
            for f in filenames:
                fp = os.path.normpath(os.path.join(dirpath, f))
                if f.endswith(".md") and fp not in WRITTEN:
                    changed.append(os.path.relpath(fp, root) + " (removed)")
                    if not check:
                        os.remove(fp)
            if not check and dirpath != base and not os.listdir(dirpath):
                os.rmdir(dirpath)

    return changed, report, papers


if __name__ == "__main__":
    root = "."
    check = "--check" in sys.argv
    for a in sys.argv[1:]:
        if not a.startswith("-"):
            root = a
    changed, report, papers = build(root, check=check)
    print("%s %d files" % ("would change" if check else "wrote", len(changed)))
    for path in changed[:8]:
        print("  ", path)
    if len(changed) > 8:
        print("   ... and %d more" % (len(changed) - 8))
    if report:
        print("\nManual review:")
        for seq, title, kind, why in report:
            print("  %02d %-45s %-14s %s" % (seq, title[:45], kind, why))
