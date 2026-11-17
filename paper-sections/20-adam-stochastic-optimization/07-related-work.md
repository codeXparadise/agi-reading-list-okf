---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/20-adam-stochastic-optimization.md
source: ../../papers/20-adam-stochastic-optimization.md
paper_title: "Adam: A Method for Stochastic Optimization"
sequence: 20
section: 5 RELATED WORK
section_role: background
section_index: 7
pages: [3, 4]
topics: ["../../topics/optimization.md"]
description: "Optimization methods bearing a direct relation to Adam are RMSProp (Tieleman & Hinton, 2012; Graves, 2013) and AdaGrad (Duchi et al., 2011); these…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5 RELATED WORK

> Section 7 of 13 from [20 - Adam: A Method for Stochastic Optimization](../../papers/20-adam-stochastic-optimization.md) · `background` · pages 3-4

Optimization methods bearing a direct relation to Adam are RMSProp (Tieleman & Hinton, 2012; Graves, 2013) and AdaGrad (Duchi et al., 2011); these relationships are discussed below. Other stochastic optimization methods include vSGD (Schaul et al., 2012), AdaDelta (Zeiler, 2012) and the natural Newton method from Roux & Fitzgibbon (2010), all setting stepsizes by estimating curvature

4

Published as a conference paper at ICLR 2015

from first-order information. The Sum-of-Functions Optimizer (SFO) (Sohl-Dickstein et al., 2014) is a quasi-Newton method based on minibatches, but (unlike Adam) has memory requirements linear in the number of minibatch partitions of a dataset, which is often infeasible on memory-constrained systems such as a GPU. Like natural gradient descent (NGD) (Amari, 1998), Adam employs a preconditioner that adapts to the geometry of the data, since bvt is an approximation to the diagonal of the Fisher information matrix (Pascanu & Bengio, 2013); however, Adam’s preconditioner (like AdaGrad’s) is more conservative in its adaption than vanilla NGD by preconditioning with the square root of the inverse of the diagonal Fisher information matrix approximation.

RMSProp: An optimization method closely related to Adam is RMSProp (Tieleman & Hinton, 2012). A version with momentum has sometimes been used (Graves, 2013). There are a few important differences between RMSProp with momentum and Adam: RMSProp with momentum generates its parameter updates using a momentum on the rescaled gradient, whereas Adam updates are directly estimated using a running average of first and second moment of the gradient. RMSProp also lacks a bias-correction term; this matters most in case of a value of β2 close to 1 (required in case of sparse gradients), since in that case not correcting the bias leads to very large stepsizes and often divergence, as we also empirically demonstrate in section 6.4.

AdaGrad: An algorithm that works well for sparse gradients is AdaGrad (Duchi et al., 2011). Its

qPt

basic version updates parameters as θt+1 = θt −α · gt/

t . Note that if we choose β2 to be

i=1 g2

infinitesimally close to 1 from below, then limβ2→1 bvt = t−1 · Pt

t . AdaGrad corresponds to a version of Adam with β1 = 0, infinitesimal (1 −β2) and a replacement of α by an annealed version

i=1 g2

q

p

t−1 · Pt

αt = α · t−1/2, namely θt −α · t−1/2 · bmt/

limβ2→1 bvt = θt −α · t−1/2 · gt/

i=1 g2

t =

qPt

t . Note that this direct correspondence between Adam and Adagrad does not hold when removing the bias-correction terms; without bias correction, like in RMSProp, a β2 infinitesimally close to 1 would lead to infinitely large bias, and infinitely large parameter updates.

i=1 g2

θt −α · gt/

---

Full document: [20 - Adam: A Method for Stochastic Optimization](../../papers/20-adam-stochastic-optimization.md) · Page-level evidence: [paper-pages/20-adam-stochastic-optimization](../../paper-pages/20-adam-stochastic-optimization/index.md)
