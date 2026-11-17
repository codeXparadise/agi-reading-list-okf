---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/20-adam-stochastic-optimization.md
source: ../../papers/20-adam-stochastic-optimization.md
paper_title: "Adam: A Method for Stochastic Optimization"
sequence: 20
section: 1 INTRODUCTION
section_role: introduction
section_index: 3
pages: [1]
topics: ["../../topics/optimization.md"]
description: "Stochastic gradient-based optimization is of core practical importance in many fields of science and engineering. Many problems in these fields can…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 1 INTRODUCTION

> Section 3 of 13 from [20 - Adam: A Method for Stochastic Optimization](../../papers/20-adam-stochastic-optimization.md) · `introduction` · pages 1-1

Stochastic gradient-based optimization is of core practical importance in many fields of science and engineering. Many problems in these fields can be cast as the optimization of some scalar parameterized objective function requiring maximization or minimization with respect to its parameters. If the function is differentiable w.r.t. its parameters, gradient descent is a relatively efficient optimization method, since the computation of first-order partial derivatives w.r.t. all the parameters is of the same computational complexity as just evaluating the function. Often, objective functions are stochastic. For example, many objective functions are composed of a sum of subfunctions evaluated at different subsamples of data; in this case optimization can be made more efficient by taking gradient steps w.r.t. individual subfunctions, i.e. stochastic gradient descent (SGD) or ascent. SGD proved itself as an efficient and effective optimization method that was central in many machine learning success stories, such as recent advances in deep learning (Deng et al., 2013; Krizhevsky et al., 2012; Hinton & Salakhutdinov, 2006; Hinton et al., 2012a; Graves et al., 2013). Objectives may also have other sources of noise than data subsampling, such as dropout (Hinton et al., 2012b) regularization. For all such noisy objectives, efficient stochastic optimization techniques are required. The focus of this paper is on the optimization of stochastic objectives with high-dimensional parameters spaces. In these cases, higher-order optimization methods are ill-suited, and discussion in this paper will be restricted to first-order methods.

We propose Adam, a method for efficient stochastic optimization that only requires first-order gradients with little memory requirement. The method computes individual adaptive learning rates for different parameters from estimates of first and second moments of the gradients; the name Adam is derived from adaptive moment estimation. Our method is designed to combine the advantages of two recently popular methods: AdaGrad (Duchi et al., 2011), which works well with sparse gradients, and RMSProp (Tieleman & Hinton, 2012), which works well in on-line and non-stationary settings; important connections to these and other stochastic optimization methods are clarified in section 5. Some of Adam’s advantages are that the magnitudes of parameter updates are invariant to rescaling of the gradient, its stepsizes are approximately bounded by the stepsize hyperparameter, it does not require a stationary objective, it works with sparse gradients, and it naturally performs a form of step size annealing.

∗Equal contribution. Author ordering determined by coin flip over a Google Hangout.

1

Published as a conference paper at ICLR 2015

Algorithm 1: Adam, our proposed algorithm for stochastic optimization. See section 2 for details, and for a slightly more efficient (but less clear) order of computation. g2

t indicates the elementwise square gt ⊙gt. Good default settings for the tested machine learning problems are α = 0.001, β1 = 0.9, β2 = 0.999 and ϵ = 10−8. All operations on vectors are element-wise. With βt

1 and βt 2 we denote β1 and β2 to the power t. Require: α: Stepsize Require: β1, β2 ∈\[0, 1): Exponential decay rates for the moment estimates Require: f(θ): Stochastic objective function with parameters θ Require: θ0: Initial parameter vector

m0 ←0 (Initialize 1st moment vector) v0 ←0 (Initialize 2nd moment vector) t ←0 (Initialize timestep) while θt not converged do

t ←t + 1 gt ←∇θft(θt−1) (Get gradients w.r.t. stochastic objective at timestep t) mt ←β1 · mt−1 + (1 −β1) · gt (Update biased first moment estimate) vt ←β2 · vt−1 + (1 −β2) · g2

t (Update biased second raw moment estimate) bmt ←mt/(1 −βt

1) (Compute bias-corrected first moment estimate) bvt ←vt/(1 −βt

2) (Compute bias-corrected second raw moment estimate) θt ←θt−1 −α · bmt/(√bvt + ϵ) (Update parameters) end while return θt (Resulting parameters)

In section 2 we describe the algorithm and the properties of its update rule. Section 3 explains our initialization bias correction technique, and section 4 provides a theoretical analysis of Adam’s convergence in online convex programming. Empirically, our method consistently outperforms other methods for a variety of models and datasets, as shown in section 6. Overall, we show that Adam is a versatile algorithm that scales to large-scale high-dimensional machine learning problems.

---

Full document: [20 - Adam: A Method for Stochastic Optimization](../../papers/20-adam-stochastic-optimization.md) · Page-level evidence: [paper-pages/20-adam-stochastic-optimization](../../paper-pages/20-adam-stochastic-optimization/index.md)
