#!/usr/bin/env python3
"""Validate an OKF v0.2 bundle and report broken internal links.

Checks:
  1. every non-reserved .md file has parseable YAML frontmatter with a non-empty `type`
  2. index.md files carry no frontmatter except okf_version at the bundle root
  3. log.md files use ISO 8601 date headings, newest first
  4. internal markdown links and image paths resolve
  5. `sequence` values are unique and match the paper filename prefix
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
        if seq:
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
    for w_ in warnings:
        print("WARN  " + w_)
    for e in errors:
        print("ERROR " + e)
    print("\n%d concept documents, %d errors, %d warnings" % (n_docs, len(errors), len(warnings)))
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
