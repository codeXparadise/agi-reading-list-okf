---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/03-scaling-laws-for-neural-language-models.md
source: ../../papers/03-scaling-laws-for-neural-language-models.md
paper_title: Scaling Laws for Neural Language Models
sequence: 3
page: 19
pages: [19]
page_of: 30
topics: ["../../topics/scaling-laws.md", "../../topics/transformer-architecture.md", "../../topics/optimization.md"]
description: "Appendices A Summary of Power Laws For easier reference, we provide a summary below of the key trends described throughout the paper. Parameters Data…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 19 of 30 - Scaling Laws for Neural Language Models

> Page 19 of the source PDF, verbatim as extracted. Canonical document: [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md)

## Appendices

## A Summary of Power Laws

For easier reference, we provide a summary below of the key trends described throughout the paper.

## Parameters Data Compute Batch Size Equation

N ∞ ∞ Fixed L (N) = (Nc/N)αN

∞ D Early Stop Fixed L (D) = (Dc/D)αD

Optimal ∞ C Fixed L (C) = (Cc/C)αC (naive)

αmin

Cmin

Nopt Dopt Cmin B ≪Bcrit L (Cmin) =

C

c /Cmin

αD

 Nc

 αN

αD + Dc

N D Early Stop Fixed L (N, D) =

N

D

αS

 Nc

αN +

Sc Smin(S,B)

N ∞ S steps B L (N, S) =

N

## Table 4

The empirical fitted values for these trends are:

## Power Law Scale (tokenization-dependent)

αN = 0.076 Nc = 8.8 × 1013 params (non-embed)

αD = 0.095 Dc = 5.4 × 1013 tokens

αC = 0.057 Cc = 1.6 × 107 PF-days

c = 3.1 × 108 PF-days

αmin

C = 0.050 Cmin

αB = 0.21 B∗= 2.1 × 108 tokens

αS = 0.76 Sc = 2.1 × 103 steps

## Table 5

The optimal parameters for compute efficient training are given by:

## Compute-Efficient Value Power Law Scale

min pN = 0.73 Ne = 1.3 · 109 params

Nopt = Ne · CpN

min pB = 0.24 Be = 2.0 · 106 tokens

B ≪Bcrit = B∗ L1/αB = BeCpB

min (lower bound) pS = 0.03 Se = 5.4 · 103 steps

Smin = Se · CpS

min (1 epoch) pD = 0.27 De = 2 · 1010 tokens

Dopt = De · CpD

## Table 6

## B Empirical Model of Compute-Efficient Frontier

Throughout this appendix all values of C, S, and αC are adjusted for training at the critical batch size Bcrit. We have left off the ‘adj’ label to avoid cluttering the notation.

## B.1 Defining Equations

The power-law fit to the learning curves implies a simple prescription for compute-efficient training. In this appendix, we will derive the optimal performance, model size, and number of training steps as a function of

---

[previous page](page-018.md) · [next page](page-020.md) · [all pages](index.md)
