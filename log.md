# Bundle Update Log

## 2026-11-18
* **Update**: Second pass on the figure crops. The first pass padded the drawing box, which still lost rotated axis labels (they sit outside it) and shaved the first and last words off captions wider than the column. The crop now snaps to the text column the figure sits in, takes every text block inside that column that touches the figure - rotated axis labels, panel titles, sub-captions, the caption itself - and only trims where a block crosses into another column. Median margin around a figure is now 26-45pt instead of 0-6pt, and no figure is cropped inside its own drawing box.
* **Update**: Re-cropped all 253 figures. Each one is now rendered from the page with 22pt of side padding and 18/24pt of vertical padding, absorbing the small text blocks that belong to the figure (axis labels, ticks, legends, annotations) and pulling the edge back rather than slicing through any line of text or a neighbouring panel in a grid figure. Filenames are unchanged, so every link in `papers/`, `paper-sections/` and `paper-pages/` still resolves.
* **Update**: Filled the eight web-sourced papers (02, 04, 08, 09, 22, 23, 26, 27). Their text is now extracted from the published pages and PDFs rather than left as a summary and a link, so every one of the 30 papers has section chunks. Paper 26 keeps its book pagination and gained 57 page chunks; paper 22 is an excerpt, marked as such in frontmatter.
* **Update**: `tools/validate_okf.py` now ignores links inside fenced code and any target with a URL scheme, so code samples in paper 02 no longer read as broken links.

## 2026-11-17
* **Update**: Added the retrieval layer - [semantic section chunks](/paper-sections/index.md) split on each paper's own headings, and [page-level evidence chunks](/paper-pages/index.md) preserving the original page text and numbering. Canonical documents in [papers](/papers/index.md) are unchanged.
* **Update**: Extended `tools/validate_okf.py` to check the retrieval layer, and added `tools/build_chunks.py` so both chunk trees regenerate deterministically from the canonical papers.
* **Creation**: Established the bundle from the 30-paper reading list curated by @rachit.speaks, with [papers](/papers/index.md), [sections](/sections/index.md), [topics](/topics/index.md), [people](/people/index.md) and [reading paths](/reading-paths/index.md).
* **Extraction**: Pulled full text and figures for 22 of the 30 papers from arXiv with PyMuPDF; added the remaining 8 as summary-plus-link concepts because no open PDF exists.
* **Creation**: Added the [seven-day orientation](/reading-paths/orientation-seven-days.md), the [sequence-models track](/reading-paths/sequence-models-to-transformers.md) and the [theory track](/reading-paths/theory-and-compression.md).
* **Update**: Added `tools/validate_okf.py` and the CI workflow that enforces OKF conformance on every push.
