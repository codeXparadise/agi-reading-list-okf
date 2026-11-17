#!/usr/bin/env python3
"""Validate an OKF v0.2 bundle and report broken internal links.

Checks:
  1. every non-reserved .md file has parseable YAML frontmatter with a non-empty `type`
  2. index.md files carry no frontmatter except okf_version at the bundle root
  3. log.md files use ISO 8601 date headings, newest first
  4. internal markdown links and image paths resolve
  5. `sequence` values are unique and match the paper filename prefix
  6. retrieval layer: every canonical paper has a section index, every paper with
     extracted full text has page chunks, external-only papers have none, and every
     chunk points back to an existing canonical document
"""
import os, re, sys

RESERVED = {"index.md", "log.md"}
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)
LINK = re.compile(r"(?<!\\)!?\[[^\]\\]*\]\(([^)]+)\)")

def split_fm(text):
    m = FM.match(text)
    if not m:
        return None, text
    return m.group(1), text[m.end():]

def yaml_get(fm, key):
    m = re.search(r"^%s:\s*(.+)$" % re.escape(key), fm, re.M)
    return m.group(1).strip() if m else None

def main(root="."):
    errors, warnings, n_docs = [], [], 0
    mds = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", "__pycache__")]
        for f in filenames:
            if f.endswith(".md"):
                mds.append(os.path.join(dirpath, f))
    seqs = {}
    for path in sorted(mds):
        rel = os.path.relpath(path, root)
        text = open(path, encoding="utf-8").read()
        fm, body = split_fm(text)
        base = os.path.basename(path)
        if base in RESERVED:
            if fm and not (base == "index.md" and os.path.dirname(rel) == ""):
                errors.append("%s: reserved file must not carry frontmatter (except okf_version at the bundle root)" % rel)
            if base == "log.md" and fm is None:
                dates = re.findall(r"^## (\d{4}-\d{2}-\d{2})$", body, re.M)
                if dates != sorted(dates, reverse=True):
                    errors.append("%s: log dates are not newest-first" % rel)
            continue
        n_docs += 1
        if fm is None:
            errors.append("%s: missing frontmatter" % rel)
            continue
        if not yaml_get(fm, "type"):
            errors.append("%s: frontmatter has no `type`" % rel)
        seq = yaml_get(fm, "sequence")
        is_chunk = (yaml_get(fm, "type") or "").strip() == "Research Paper Chunk"
        if seq and not is_chunk:
            seq = seq.strip()
            if seq in seqs:
                errors.append("%s: duplicate sequence %s (also %s)" % (rel, seq, seqs[seq]))
            seqs[seq] = rel
            prefix = base.split("-")[0]
            if prefix.isdigit() and int(prefix) != int(seq):
                errors.append("%s: filename prefix %s does not match sequence %s" % (rel, prefix, seq))
        # links
        for target in LINK.findall(body):
            target = target.split("#")[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("/"):
                resolved = os.path.join(root, target.lstrip("/"))
            else:
                resolved = os.path.normpath(os.path.join(os.path.dirname(path), target))
            if not os.path.exists(resolved):
                warnings.append("%s: unresolved link -> %s" % (rel, target))
    n_chunks = check_retrieval_layer(root, errors, warnings)

    for w_ in warnings:
        print("WARN  " + w_)
    for e in errors:
        print("ERROR " + e)
    print("\n%d concept documents, %d retrieval chunks, %d errors, %d warnings"
          % (n_docs, n_chunks, len(errors), len(warnings)))
    return 1 if errors else 0

def check_retrieval_layer(root, errors, warnings):
    """Verify paper-sections/ and paper-pages/ agree with the canonical papers."""
    papers_dir = os.path.join(root, "papers")
    if not os.path.isdir(papers_dir):
        return 0
    sec_root = os.path.join(root, "paper-sections")
    page_root = os.path.join(root, "paper-pages")
    n_chunks = 0
    canon = {}
    for name in sorted(os.listdir(papers_dir)):
        if not name.endswith(".md") or name == "index.md":
            continue
        slug = name[:-3]
        text = open(os.path.join(papers_dir, name), encoding="utf-8").read()
        fm, body = split_fm(text)
        if fm is None:
            continue
        canon[slug] = {
            "sequence": yaml_get(fm, "sequence") or "",
            "full_text": (re.search(r"^\s*full_text:\s*(\S+)", fm, re.M).group(1)
                          if re.search(r"^\s*full_text:\s*(\S+)", fm, re.M) else ""),
            "pages": len(re.findall(r"^<!-- page (\d+) -->$", body, re.M)),
        }

    for slug, meta in sorted(canon.items(), key=lambda kv: int(kv[1]["sequence"] or 0)):
        sec_idx = os.path.join(sec_root, slug, "index.md")
        page_idx = os.path.join(page_root, slug, "index.md")
        if not os.path.isfile(sec_idx):
            errors.append("paper-sections/%s/index.md: missing section index for papers/%s.md" % (slug, slug))
        if not os.path.isfile(page_idx):
            errors.append("paper-pages/%s/index.md: missing page index for papers/%s.md" % (slug, slug))
        chunks = []
        if os.path.isdir(os.path.join(sec_root, slug)):
            chunks += [os.path.join(sec_root, slug, f) for f in sorted(os.listdir(os.path.join(sec_root, slug)))
                       if f != "index.md"]
        page_files = []
        if os.path.isdir(os.path.join(page_root, slug)):
            page_files = [f for f in sorted(os.listdir(os.path.join(page_root, slug)))
                          if f.startswith("page-") and f.endswith(".md")]
            chunks += [os.path.join(page_root, slug, f) for f in page_files]

        external = "external-only" in meta["full_text"]
        if external:
            if page_files:
                errors.append("paper-pages/%s: %d page chunks for a summary/link-only paper (no full text to cite)"
                              % (slug, len(page_files)))
            if meta["pages"]:
                errors.append("papers/%s.md: external-only paper contains %d page markers" % (slug, meta["pages"]))
        else:
            if not page_files:
                errors.append("paper-pages/%s: extracted paper has no page chunks" % slug)
            elif len(page_files) != meta["pages"]:
                errors.append("paper-pages/%s: %d page chunks but the canonical document has %d page markers"
                              % (slug, len(page_files), meta["pages"]))
            if not chunks:
                errors.append("paper-sections/%s: extracted paper has no semantic section chunks" % slug)

        for path in chunks:
            rel = os.path.relpath(path, root)
            n_chunks += 1
            text = open(path, encoding="utf-8").read()
            fm, _ = split_fm(text)
            if fm is None:
                errors.append("%s: chunk has no frontmatter" % rel)
                continue
            if (yaml_get(fm, "type") or "").strip() != "Research Paper Chunk":
                errors.append("%s: chunk type is not `Research Paper Chunk`" % rel)
            for key in ("paper", "source"):
                target = (yaml_get(fm, key) or "").strip().strip('"')
                if not target:
                    errors.append("%s: chunk has no `%s`" % (rel, key))
                    continue
                resolved = os.path.normpath(os.path.join(os.path.dirname(path), target))
                if not os.path.isfile(resolved):
                    errors.append("%s: `%s` does not resolve to a canonical paper (%s)" % (rel, key, target))
                elif os.path.basename(resolved) != slug + ".md":
                    errors.append("%s: `%s` points at the wrong paper (%s)" % (rel, key, target))
            seq = (yaml_get(fm, "sequence") or "").strip()
            if seq and seq != meta["sequence"]:
                errors.append("%s: chunk sequence %s does not match the paper's %s" % (rel, seq, meta["sequence"]))
            ctype = (yaml_get(fm, "chunk_type") or "").strip()
            if ctype == "page":
                m = re.match(r"page-(\d+)\.md$", os.path.basename(path))
                page = (yaml_get(fm, "page") or "").strip()
                if not m or m.group(1).lstrip("0") != page.lstrip("0"):
                    errors.append("%s: page number in filename, frontmatter and body disagree" % rel)
            elif ctype != "semantic-section":
                errors.append("%s: unknown chunk_type `%s`" % (rel, ctype))
    return n_chunks


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
