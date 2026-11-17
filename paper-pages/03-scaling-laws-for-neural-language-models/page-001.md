---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/03-scaling-laws-for-neural-language-models.md
source: ../../papers/03-scaling-laws-for-neural-language-models.md
paper_title: Scaling Laws for Neural Language Models
sequence: 3
page: 1
pages: [1]
page_of: 30
topics: ["../../topics/scaling-laws.md", "../../topics/transformer-architecture.md", "../../topics/optimization.md"]
description: "Contents 1 Introduction 2 2 Background and Methods 6 3 Empirical Results and Basic Power Laws 7 4 Charting the Infinite Data Limit and Overfitting 10…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 1 of 30 - Scaling Laws for Neural Language Models

> Page 1 of the source PDF, verbatim as extracted. Canonical document: [03 - Scaling Laws for Neural Language Models](../../papers/03-scaling-laws-for-neural-language-models.md)

## Contents

## 1 Introduction 2

## 2 Background and Methods 6

## 3 Empirical Results and Basic Power Laws 7

## 4 Charting the Infinite Data Limit and Overfitting 10

## 5 Scaling Laws with Model Size and Training Time 12

## 6 Optimal Allocation of the Compute Budget 14

## 7 Related Work 18

## 8 Discussion 18

## Appendices 20

## A Summary of Power Laws 20

## B Empirical Model of Compute-Efficient Frontier 20

## C Caveats 22

## D Supplemental Figures 23

## 1 Introduction

Language provides a natural domain for the study of artificial intelligence, as the vast majority of reasoning tasks can be efficiently expressed and evaluated in language, and the world’s text provides a wealth of data for unsupervised learning via generative modeling. Deep learning has recently seen rapid progress in language modeling, with state of the art models \[RNSS18, DCLT18, YDY+19, LOG+19, RSR+19\] approaching human-level performance on many specific tasks \[WPN+19\], including the composition of coherent multiparagraph prompted text samples \[RWC+19\].

One might expect language modeling performance to depend on model architecture, the size of neural models, the computing power used to train them, and the data available for this training process. In this work we will empirically investigate the dependence of language modeling loss on all of these factors, focusing on the Transformer architecture \[VSP+17, LSP+18\]. The high ceiling and low floor for performance on language tasks allows us to study trends over more than seven orders of magnitude in scale.

Throughout we will observe precise power-law scalings for performance as a function of training time, context length, dataset size, model size, and compute budget.

## 1.1 Summary

Our key findings for Transformer language models are are as follows:

2Here we display predicted compute when using a sufficiently small batch size. See Figure 13 for comparison to the purely empirical data.

---

first page · [next page](page-002.md) · [all pages](index.md)
