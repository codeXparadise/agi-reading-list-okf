# Bundle Update Log

## 2026-11-17
* **Update**: Added the retrieval layer - [semantic section chunks](/paper-sections/index.md) split on each paper's own headings, and [page-level evidence chunks](/paper-pages/index.md) preserving the original page text and numbering. Canonical documents in [papers](/papers/index.md) are unchanged.
* **Update**: Extended `tools/validate_okf.py` to check the retrieval layer, and added `tools/build_chunks.py` so both chunk trees regenerate deterministically from the canonical papers.
* **Creation**: Established the bundle from the 30-paper reading list curated by @rachit.speaks, with [papers](/papers/index.md), [sections](/sections/index.md), [topics](/topics/index.md), [people](/people/index.md) and [reading paths](/reading-paths/index.md).
* **Extraction**: Pulled full text and figures for 22 of the 30 papers from arXiv with PyMuPDF; added the remaining 8 as summary-plus-link concepts because no open PDF exists.
* **Creation**: Added the [seven-day orientation](/reading-paths/orientation-seven-days.md), the [sequence-models track](/reading-paths/sequence-models-to-transformers.md) and the [theory track](/reading-paths/theory-and-compression.md).
* **Update**: Added `tools/validate_okf.py` and the CI workflow that enforces OKF conformance on every push.
