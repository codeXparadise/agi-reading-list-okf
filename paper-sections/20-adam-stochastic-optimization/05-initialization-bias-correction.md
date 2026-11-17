---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/20-adam-stochastic-optimization.md
source: ../../papers/20-adam-stochastic-optimization.md
paper_title: "Adam: A Method for Stochastic Optimization"
sequence: 20
section: 3 INITIALIZATION BIAS CORRECTION
section_role: other
section_index: 5
pages: [2, 3]
topics: ["../../topics/optimization.md"]
description: "As explained in section 2, Adam utilizes initialization bias correction terms. We will here derive the term for the second moment estimate; the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3 INITIALIZATION BIAS CORRECTION

> Section 5 of 13 from [20 - Adam: A Method for Stochastic Optimization](../../papers/20-adam-stochastic-optimization.md) · `other` · pages 2-3

As explained in section 2, Adam utilizes initialization bias correction terms. We will here derive the term for the second moment estimate; the derivation for the first moment estimate is completely analogous. Let g be the gradient of the stochastic objective f, and we wish to estimate its second raw moment (uncentered variance) using an exponential moving average of the squared gradient, with decay rate β2. Let g1, ..., gT be the gradients at subsequent timesteps, each a draw from an underlying gradient distribution gt ∼p(gt). Let us initialize the exponential moving average as v0 = 0 (a vector of zeros). First note that the update at timestep t of the exponential moving average vt = β2 · vt−1 + (1 −β2) · g2

t indicates the elementwise square gt ⊙gt) can be written as a function of the gradients at all previous timesteps:

t (where g2

t X

βt−i

2 · g2 i (1)

vt = (1 −β2)

i=1

We wish to know how E\[vt\], the expected value of the exponential moving average at timestep t, relates to the true second moment E\[g2

t \], so we can correct for the discrepancy between the two. Taking expectations of the left-hand and right-hand sides of eq. (1):

"

#

t X

βt−i

2 · g2 i

E\[vt\] = E

(2)

(1 −β2)

i=1

t X

βt−i

= E\[g2

2 + ζ (3)

t \] · (1 −β2)

i=1

= E\[g2

t \] · (1 −βt

2) + ζ (4)

i \] is stationary; otherwise ζ can be kept small since the exponential decay rate β1 can (and should) be chosen such that the exponential moving average assigns small weights to gradients too far in the past. What is left is the term (1 −βt

where ζ = 0 if the true second moment E\[g2

2) which is caused by initializing the running average with zeros. In algorithm 1 we therefore divide by this term to correct the initialization bias.

In case of sparse gradients, for a reliable estimate of the second moment one needs to average over many gradients by chosing a small value of β2; however it is exactly this case of small β2 where a lack of initialisation bias correction would lead to initial steps that are much larger.

3

Published as a conference paper at ICLR 2015

---

Full document: [20 - Adam: A Method for Stochastic Optimization](../../papers/20-adam-stochastic-optimization.md) · Page-level evidence: [paper-pages/20-adam-stochastic-optimization](../../paper-pages/20-adam-stochastic-optimization/index.md)
