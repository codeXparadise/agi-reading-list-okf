---
type: Guide
title: Agent guide
description: How an agent should traverse this bundle, answer from it, and cite it back to the original page.
tags: [documentation, agents, okf]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Agent guide

This file is instructions for a machine reader. A human can skip it and read [README.md](README.md) instead.

## What this bundle is

An OKF v0.2 knowledge bundle: markdown files with YAML frontmatter, one concept per file, relationships expressed as markdown links. There is no retrieval index to build first and no schema to import. Read the tree.

## Traversal

1. Read [index.md](index.md). It carries `okf_version` and the top-level map.
2. For a question about a paper, go to [papers/index.md](papers/index.md) - it lists all 30 with a one-line description each, which is usually enough to choose without opening anything.
3. For a question about an idea rather than a paper, go to [topics/index.md](topics/index.md).
4. When a paper's prerequisites matter, follow its `builds_on` links; when a question is about consequences, follow `enables`.

Do not enumerate the whole tree before answering. OKF is designed for progressive disclosure: the indexes exist so you can open two or three files, not thirty.

## Answering from frontmatter

Frontmatter is authoritative and cheap to parse. Prefer it over prose:

- `title`, `authors`, `year`, `venue` - identity. Answer "who wrote X" from here.
- `sequence` - the paper's position in the list, 1 to 30.
- `section` - which of the five thematic groups it belongs to.
- `resource` - the canonical URL. Always prefer this over any link found in the body.
- `arxiv` - the arXiv identifier, when one exists.
- `topics`, `builds_on`, `enables` - the graph, as bundle-absolute paths.
- `extraction.full_text` - `extracted` or `external-only`. If it is `external-only`, the body has a summary and a link but no full text; do not answer detailed technical questions from it, and say so.

## Citing

Cite a paper by its sequence number and title, and when you quote the body, cite the page marker nearest the quoted text. The full text carries `<!-- page N -->` comments at every original page boundary, so a claim taken from between two markers comes from the earlier one.

When a user asks for a source, give `resource` from the frontmatter, not a link you found in prose.

## Trust and freshness

Every concept carries `generated` (who wrote it, when) and `verified` (what confirmed it). Papers are stable artefacts: the `verified` entry records that the extraction was checked, not that the paper's claims were reviewed. Do not describe a paper as "verified" to a user; describe the bundle's extraction as checked.

## What not to do

- Do not treat this bundle as a substitute for the original papers when precision matters. Equations were extracted as plain text, so mathematical statements are approximate. Point the user at `resource` for exact notation.
- Do not invent papers, authors or years that are not in frontmatter. If a question is outside the 30, say so.
- Do not rewrite files to "fix" a broken link: OKF explicitly tolerates links to concepts that do not exist yet.

## Building an agent on this corpus

The intended use is a reading companion: a user brings their own model (hosted API or self-hosted), points it at this repository, and asks questions across the list. A workable pattern:

1. **Load metadata only** for all 30 papers from frontmatter at start-up. That is small enough to keep in context.
2. **Retrieve** one paper document when a question needs detail, using `papers/index.md` descriptions as the first-pass router.
3. **Chunk by page marker** if the model has a small window: each `<!-- page N -->` block is a natural chunk with its own citation.
4. **Follow the graph** when a question spans papers: `builds_on` for prerequisites, `topics` for related work.

Because the format is plain files, the same corpus works behind a git checkout, a static site, or a filesystem tool with no changes.
