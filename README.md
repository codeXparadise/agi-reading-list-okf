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
| `papers/` | One concept document per paper: overview, full extracted text, figures inline, relationships, provenance |
| `sections/` | The five thematic groups of the original list |
| `topics/` | 19 cross-cutting concepts - attention, scaling laws, memory, MDL, Kolmogorov complexity, generative models |
| `people/` | The researchers behind the papers, with the papers each one wrote |
| `reading-paths/` | Three curated routes: a seven-day orientation, the sequence-model lineage, and the theory track |
| `references/` | Provenance: the original reading list as a concept document |
| `assets/` | Figures extracted from the PDFs, numbered by paper |
| `tools/` | `validate_okf.py` - checks the bundle for OKF conformance and broken links |

## How it was built

1. The list was read from the source PDF and the 30 items were identified, in order, with their authors, venues and canonical links.
2. Each paper was fetched from arXiv where an open version exists, then text and figures were extracted page by page with PyMuPDF. Raster figures are lifted directly; vector figures are detected through their captions and rendered at 150 dpi, so plots that are drawn rather than embedded survive too.
3. Every paper became a concept document with frontmatter carrying its identity (`type`, `title`, `resource`, `year`, `venue`), its position (`sequence`, `section`), its provenance (`sources`, `generated`, `verified`) and its place in the graph (`builds_on`, `enables`, `topics`).
4. Indexes, the log, and the repository documentation were generated from the same metadata, so the tree and the graph can never disagree.

22 of the 30 items are open PDFs and carry full text plus figures. The other 8 - *The Annotated Transformer*, AlexNet, Karpathy's RNN essay, Olah's LSTM post, *The First Law of Complexodynamics*, the 1993 Hinton and van Camp paper, the Kolmogorov complexity book and Legg's thesis - are not distributed as open PDFs, so their concept documents carry a summary and a canonical link rather than republished text.

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

The validator checks the OKF conformance rules (every non-reserved markdown file has frontmatter with a non-empty `type`; `index.md` and `log.md` follow their reserved structure) and additionally reports broken internal links and papers whose frontmatter sequence does not match their filename. It runs in CI on every push.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The short version: edit the metadata in `data.py`-equivalent frontmatter, regenerate indexes, run the validator, open a PR.

## Copyright and licensing

The bundle's own prose, structure and metadata are released under CC BY 4.0. The papers themselves are not: each remains under the licence its authors and publisher set. Full texts and figures are included here so the corpus is usable offline; before making this repository public, check the licence of each paper (arXiv papers are variously under arXiv's non-exclusive licence, CC BY, or publisher copyright) and consider linking rather than republishing where the licence does not allow it. A private repository, or a bundle that keeps `full_text: external-only` for those papers, avoids the question entirely.

## Attribution

Reading list curated by @rachit.speaks. Format specification: [Open Knowledge Format v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format).
