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

## Retrieval workflow

Answer from the smallest layer that can carry the answer. Do not load a canonical paper to answer a question about one section of it.

```
user query
  -> papers/index.md or topics/index.md     (identify the paper)
  -> paper-sections/<paper>/index.md        (pick 1-3 sections by heading and role)
  -> paper-pages/<paper>/page-NNN.md        (only for exact evidence)
  -> answer, naming the paper and the nearest page marker
```

1. **Identify the paper.** [papers/index.md](papers/index.md) lists all 30 with a one-line description; [topics/index.md](topics/index.md) routes an idea ("why does compression imply generalisation?") to papers. Usually nothing else needs opening.
2. **Retrieve semantic chunks first.** Each paper has a [section index](paper-sections/index.md) listing its sections in the paper's own order, with a `section_role` (`abstract`, `introduction`, `background`, `method`, `experiments`, `results`, `limitations`, `conclusion`, `references`, `appendix`, `other`) and a page range. Open one to three of these - they are small enough to read whole, and each carries its own frontmatter with `paper`, `paper_title`, `sequence`, `section` and `pages`.
3. **Drop to page chunks only when the answer must be exact.** A quotation, an equation as printed, a figure reference, a table value or a citation needs [paper-pages](paper-pages/index.md): one chunk per page of the source PDF, text verbatim, with `page` and `page_of` in frontmatter. They are bigger and noisier than section chunks, so they are the wrong first move for a conceptual question.
4. **Open the canonical document last.** `papers/*.md` is the authoritative complete document - frontmatter, overview, full text, figures, relationships. Read it when the question spans the whole paper, or when you need to check that a chunk has not lost context.

Do not enumerate the whole tree before answering. OKF is designed for progressive disclosure: the indexes exist so you can open two or three files, not thirty.

### Which layer answers which question

| Question | Layer |
| --- | --- |
| "What is this paper about?" / "Which paper covers attention?" | `papers/index.md` |
| "What does the paper say about the model architecture?" | `paper-sections/<paper>/05-model-architecture.md` |
| "How did they evaluate it, and on what data?" | the `experiments` / `results` section chunks |
| "What were the limitations?" | the `limitations` section chunk, or `conclusion` if the paper has none |
| "Quote the exact sentence on page 4" / "What is equation 3?" | `paper-pages/<paper>/page-004.md` |
| "How does this relate to paper 14?" | the canonical document's Relationships section, or `topics/` |

### Naming a citation

Give the paper title, the section, and the page: *Attention Is All You Need, §3 Model Architecture, p. 3*. The page comes from `pages` on a section chunk or `page` on a page chunk; both are the original PDF page, not the chunk's position.

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

## Web-sourced papers

Eight items - 02, 04, 08, 09, 22, 23, 26, 27 - were extracted from the web rather than from arXiv. They have section chunks like every other paper, so answer from those normally. Two differences matter when you cite:

- **No page numbers.** Their `paper-pages/<paper>/index.md` says no page chunks exist, because a web page carries no original pagination. Cite the section, not a page. The exception is paper 26, the Kolmogorov book, whose open PDF is paginated: it has page chunks and you may cite them.
- **Figures vary by paper.** Check `figures.local` and `figures.remote` in the paper's frontmatter. Papers 02, 08, 09 and 22 have local images under `assets/`; a few oversized ones and the four PDF-only papers (04, 23, 26, 27) keep their figures in the original source. If `figures.local` is 0, quote the caption and surrounding text rather than describing an image you cannot see.

Paper 22, *The First Law of Complexodynamics*, is an **excerpt**: the opening argument and the closing passage, with the middle of the essay at the link. Do not summarise it as if you had the whole essay; say that the bundle holds an excerpt.

Papers 26 and 22 also carry `extraction.coverage` in frontmatter (`pages 1-85 of 519`, `excerpt`). Check it before claiming the bundle holds a paper in full.

## What not to do

- Do not cite a page number from a section chunk's own position; use its `pages` field, which is the original PDF page range.
- Do not treat this bundle as a substitute for the original papers when precision matters. Equations were extracted as plain text, so mathematical statements are approximate. Point the user at `resource` for exact notation.
- Do not invent papers, authors or years that are not in frontmatter. If a question is outside the 30, say so.
- Do not rewrite files to "fix" a broken link: OKF explicitly tolerates links to concepts that do not exist yet.

## Building an agent on this corpus

The intended use is a reading companion: a user brings their own model (hosted API or self-hosted), points it at this repository, and asks questions across the list. A workable pattern:

1. **Load metadata only** for all 30 papers from frontmatter at start-up. That is small enough to keep in context.
2. **Retrieve a section chunk** when a question needs detail, using the section indexes as the second-pass router: the heading, the role and the page range are enough to choose without reading the body.
3. **Fall back to page chunks** for verbatim evidence, and to the canonical document when the question spans the whole paper. Both chunk trees are plain files, so a keyword or embedding index over `paper-sections/` and `paper-pages/` is a drop-in if you want one - the bundle ships none and needs none.
4. **Follow the graph** when a question spans papers: `builds_on` for prerequisites, `topics` for related work.

Because the format is plain files, the same corpus works behind a git checkout, a static site, or a filesystem tool with no changes.
