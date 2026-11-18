---
type: Documentation
title: AI Research Papers - OKF Knowledge Bundle
description: An OKF v0.2 knowledge base of the 30-paper AGI reading list, with full extracted text, figures and a relationship graph, built so anyone can stand an agent on top of it.
tags: [documentation, okf, knowledge-base, agi, reading-list]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# AI Research Papers - an OKF knowledge bundle

Thirty papers, one repository, one format that both a human and an agent can read without any tooling. This is the reading list curated by [@rachit.speaks](https://github.com/rachit-speaks) - the list Ilya Sutskever is reported to have given John Carmack, with the line that if you really learn all of these, you will know 90% of what matters today - turned into a structured knowledge base instead of a folder of PDFs.

The bundle follows **Open Knowledge Format (OKF) v0.2**, the minimal convention from Google Cloud for agent-readable knowledge: a directory of markdown files with YAML frontmatter, an `index.md` in every directory, and relationships expressed as ordinary links. No SDK, no database, no build step. If you can `cat` a file you can read it; if you can `git clone` it you can ship it.

## What is inside

| Path | What it holds |
| --- | --- |
| `papers/` | The canonical document per paper: overview, full extracted text, figures inline, relationships, provenance. Authoritative and complete |
| `paper-sections/` | **Retrieval layer 1.** Each paper split on its own headings into semantic chunks - abstract, introduction, method, experiments, results, limitations, conclusion - with role, sequence and page range in frontmatter |
| `paper-pages/` | **Retrieval layer 2.** One chunk per page of the source PDF, text verbatim, original page number preserved. For exact quotations, equations, figures and citations |
| `sections/` | The five thematic groups of the original list |
| `topics/` | 19 cross-cutting concepts - attention, scaling laws, memory, MDL, Kolmogorov complexity, generative models |
| `people/` | The researchers behind the papers, with the papers each one wrote |
| `reading-paths/` | Three curated routes: a seven-day orientation, the sequence-model lineage, and the theory track |
| `references/` | Provenance: the original reading list as a concept document |
| `assets/` | Figures extracted from the PDFs, numbered by paper |
| `tools/` | `validate_okf.py` - checks the bundle for OKF conformance and broken links |

## Three layers, one corpus

The bundle is built for retrieval, not just for reading. Every paper exists at three levels of granularity, and an agent is expected to answer from the smallest one that can carry the answer:

| Layer | Path | Size | Use it for |
| --- | --- | --- | --- |
| Semantic sections | `paper-sections/<paper>/` | 567 chunks | "What does it say about X?" - one to three chunks answer most questions |
| Page evidence | `paper-pages/<paper>/` | 495 chunks, 23 papers | Exact quotations, equations as printed, figure references, citations |
| Canonical document | `papers/<paper>.md` | 30 documents | Whole-paper questions, and checking a chunk has not lost context |

The section chunks are not character-count windows: they follow the paper's own headings, in the paper's own order, with the heading text preserved in `section` and mapped to a `section_role`. Headings that are not real sections - titles, author lines, figure labels, table-of-contents lines, stray math - are rejected and their text merged into the preceding chunk, so nothing is lost and no structure is invented. A paper whose headings were too sparse to trust gets one conservative whole-text chunk rather than a fabricated outline.

Each chunk carries its provenance in frontmatter:

```yaml
type: Research Paper Chunk
chunk_type: semantic-section     # or: page
paper: ../../papers/01-attention-is-all-you-need.md
source: ../../papers/01-attention-is-all-you-need.md
paper_title: Attention Is All You Need
sequence: 1
section: 3 Model Architecture
section_role: method
pages: [2, 3, 4, 5]
topics: ["../../topics/attention.md"]
```

Page chunks additionally carry `page` and `page_of`. Figures are not duplicated: page chunks keep the same `../../assets/...` links the canonical document uses.

Eight papers (02, 04, 08, 09, 22, 23, 26, 27) came from the web rather than arXiv. They have section chunks like every other paper; only paper 26 has page chunks, because only it has real pagination. Their page index states that no page chunks exist and why, so an agent cannot invent page-level evidence for them.

## How it was built

1. The list was read from the source PDF and the 30 items were identified, in order, with their authors, venues and canonical links.
2. Each paper was fetched from arXiv where an open version exists, then text and figures were extracted page by page with PyMuPDF. Every figure - embedded raster image or vector drawing found through its caption - is rendered from the page at 200 dpi, not dumped as the raw embedded bitmap, so labels the PDF draws as separate text objects survive. The crop snaps to the text column the figure sits in and takes every text block inside that column that touches the figure: rotated axis labels, tick rows, legends, panel titles, sub-captions and the caption itself. It only trims where a block crosses into another column, and it never crops inside the figure's own drawing box or into a neighbouring panel of a grid figure.
3. Every paper became a concept document with frontmatter carrying its identity (`type`, `title`, `resource`, `year`, `venue`), its position (`sequence`, `section`), its provenance (`sources`, `generated`, `verified`) and its place in the graph (`builds_on`, `enables`, `topics`).
4. Indexes, the log, and the repository documentation were generated from the same metadata, so the tree and the graph can never disagree.
5. The retrieval layer was generated from the canonical documents by `tools/build_chunks.py`: sections from each paper's own headings, pages from the `<!-- page N -->` markers. Both trees are deterministic - the same input produces byte-identical output, and CI fails if they drift.

All 30 papers carry full text. Twenty-two were extracted from open PDFs with PyMuPDF; the other eight - *The Annotated Transformer*, AlexNet, Karpathy's RNN essay, Olah's LSTM post, *The First Law of Complexodynamics*, the 1993 Hinton and van Camp paper, the Kolmogorov complexity book and Legg's thesis - are not distributed as open PDFs on arXiv, so their text was extracted from their published web pages and PDFs on the authors' own sites and folded into the same shape.

Their figures are handled per paper, and every paper's frontmatter says which case it is in (`figures.local`, `figures.remote`, `figures.note`):

| Papers | Figures |
| --- | --- |
| 02, 08, 09, 22 | 41 images pulled into `assets/` as local files |
| 02 (3), 08 (6), 09 (3) | the largest source images stay linked to the original: the transfer path caps at about 190 KB per file and these are bigger |
| 04, 23, 26, 27 | no figures: the source PDFs run from 1.4 MB to 10 MB, well past that cap, so the figures stay in the original |
| 11 | genuinely has no figures - the paper is text and tables |

The eight also carry no page chunks, because a web page has no original page numbers and inventing them would make citations wrong. The exception is the Kolmogorov book, whose open PDF has real pagination - pages 1-85 of 519 were fetched, and those page numbers are preserved as `<!-- page N -->` markers, so it has page chunks. The reading list points at chapter 14 (p. 425), which falls outside the fetched range; the link is in the document. *The First Law of Complexodynamics* is the one excerpt rather than a full text: the page extractor capped the fetch, so the document holds the opening argument and the closing passage, with the full essay at the link.

## Reading it as a human

Start at [index.md](index.md), or jump straight into a [reading path](reading-paths/index.md). The seven-day orientation is the shortest route that still leaves you with the shape of the field.

## Reading it as an agent

[AGENTS.md](AGENTS.md) is written for the agent, not the human: traversal order, how to cite a paper back to its page, how to answer from frontmatter instead of guessing, and what to do when a paper is link-only. The short version: start at `index.md`, use `papers/index.md` for progressive disclosure, and follow `builds_on` when a question needs prerequisites.

## Using it as a corpus

The bundle is deliberately boring to consume:

```python
import frontmatter, pathlib

papers = []
for f in sorted(pathlib.Path("papers").glob("*.md")):
    if f.name == "index.md":
        continue
    post = frontmatter.load(f)
    papers.append({"meta": post.metadata, "body": post.content})
```

That is enough to build retrieval, a chat agent, or an evaluation set. Nothing in the format assumes a particular runtime, and every field beyond `type` is optional, so a consumer that only understands `title` and the body still works.

## Validating

```bash
python tools/validate_okf.py .
```

The validator checks the OKF conformance rules (every non-reserved markdown file has frontmatter with a non-empty `type`; `index.md` and `log.md` follow their reserved structure), reports broken internal links, and checks the retrieval layer: every canonical paper has a section index, every extracted paper has one page chunk per source page, external-only papers have none, and every chunk's `paper`, `source` and `sequence` point back to the right canonical document.

To regenerate the chunk trees after editing a paper:

```bash
python tools/build_chunks.py .          # rewrite paper-sections/ and paper-pages/
python tools/build_chunks.py . --check  # report what would change, write nothing
```

CI runs both, and fails if regenerating produces a diff.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The short version: edit the metadata in `data.py`-equivalent frontmatter, regenerate indexes, run the validator, open a PR.

## Copyright and licensing

The bundle's own prose, structure and metadata are released under CC BY 4.0. The papers themselves are not: each remains under the licence its authors and publisher set. Full texts and figures are included here so the corpus is usable offline; before making this repository public, check the licence of each paper (arXiv papers are variously under arXiv's non-exclusive licence, CC BY, or publisher copyright) and consider linking rather than republishing where the licence does not allow it. A private repository, or a bundle that keeps `full_text: external-only` for those papers, avoids the question entirely.

## Attribution

Reading list curated by @rachit.speaks. Format specification: [Open Knowledge Format v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format).
