---
type: Guide
title: Contributing
description: How to correct metadata, add a paper, or fix an extraction in this bundle without breaking OKF conformance.
tags: [documentation, contributing]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Contributing

## Ground rules

- Every non-reserved `.md` file keeps a YAML frontmatter block with a non-empty `type`. This includes `README.md`, this file and `AGENTS.md`: OKF conformance is a property of the whole tree, and an exception for repository documentation would break it.
- `index.md` and `log.md` are reserved. An index carries no frontmatter except `okf_version` at the bundle root. A log is a date-grouped list, newest first.
- Links between concepts are bundle-absolute (`/papers/01-attention-is-all-you-need.md`), so files can move within their directory without breaking the graph.

## Common changes

**Correct a fact about a paper.** Edit its frontmatter (`authors`, `year`, `venue`, `resource`) and add a `verified` entry with your actor id, for example `human:yourhandle`. Do not delete the previous verification entry.

**Add a paper to the list.** Create `papers/31-<slug>.md` with the standard frontmatter, add it to the right section's `papers` list, add it to `papers/index.md` and to the section document's paper list, then add its edges to the papers it builds on and enables.

**Fix an extraction.** Text and figures are generated; edit the generator rather than the output where you can, and re-run the validator afterwards. If you edit a document by hand, bump `generated.at`.

**Never hand-edit `paper-sections/` or `paper-pages/`.** They are generated from `papers/*.md` by `tools/build_chunks.py`; edit the canonical document and regenerate:

```bash
python tools/build_chunks.py . && python tools/validate_okf.py .
```

A chunk tree that differs from what the generator produces fails CI.

**Add a topic or a person.** Same shape as the existing ones: frontmatter with `type`, a `papers` list, and a body that links back. Add it to the matching `index.md`.

## Before opening a pull request

```bash
python tools/validate_okf.py .
```

The validator must pass. It checks frontmatter presence and `type`, reserved-file structure, internal link targets, and that `sequence` values are unique and match filenames. CI runs the same command.

## Licensing of contributions

Prose and metadata you add are contributed under CC BY 4.0. Do not add material whose licence you cannot meet.
