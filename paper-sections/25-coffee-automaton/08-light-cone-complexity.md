---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/25-coffee-automaton.md
source: ../../papers/25-coffee-automaton.md
paper_title: "Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton"
sequence: 25
section: 2.4 Light-Cone Complexity
section_role: other
section_index: 8
pages: [6, 7]
topics: ["../../topics/kolmogorov-complexity.md"]
description: "The final complexity measure we consider was proposed by Shalizi, Shalizi, and Haslinger [12]; we call it light-cone complexity. In contrast to the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.4 Light-Cone Complexity

> Section 8 of 21 from [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](../../papers/25-coffee-automaton.md) · `other` · pages 6-7

The final complexity measure we consider was proposed by Shalizi, Shalizi, and Haslinger \[12\]; we call it light-cone complexity. In contrast to the previous measures, light-cone complexity does not even try to define the “complexity” of a string x, given only x itself. Instead, the definition of light-cone complexity assumes a causal structure: that is, a collection of spacetime points A (assumed to be fixed), together with a transitive, cycle-free binary relation indicating which points a ∈A are to the “future” of which other points in A. The set of all points b ∈A to a’s future is called a’s future light-cone, and is denoted F (a). The set of all points b ∈A to a’s past (that is, such that a is to b’s future) is called a’s past light-cone, and is denoted P (a). For example, if we were studying the evolution of a 1-dimensional cellular automaton, then A would consist of all ordered pairs (x, t) (where x is position and t is time), and we would have

F (x, t) = {(y, u) : u > t, |x −y| ≤u −t} , (4)

P (x, t) = {(y, u) : u < t, |x −y| ≤t −u} . (5)

Now given a spacetime point a ∈A, let Va be the actual value assumed by the finite automaton at a (for example, “alive” or “dead,” were we discussing Conway’s Game of Life or some other 2-state system). In general, the finite automaton might be probabilistic, in which case Va is a random variable, with a Shannon entropy H (Va) and so forth. Also, given a set S ⊆A, let VS := (Va)a∈S be a complete description of the values at all points in S. Then the light-cone complexity at a point a ∈A, or LCC (a), can be defined as follows:

LCC (a) = I

VP(a) : VF(a)

(6)

−H

= H

VP(a)

+ H

VF(a)

VP(a), VF(a)

. (7)

In other words, LCC (a) is the mutual information between a’s past and future light-cones: the number of bits about a’s future that are encoded by its past. If we want the light-cone complexity of (say) an entire spatial slice, we could then take the sum of LCC (a) over all a in that slice, or some other combination.

The intuition here is that, if the cellular automaton dynamics are “too simple,” then LCC (a) will be small simply because H

are both small. Conversely, if the dynamics are “too random,” then LCC (a) will be small because H

VP(a)

and H

VF(a)

≈H

: although the past and future light-cones both have plenty of entropy, they are uncorrelated, so that knowledge of the past is of barely any use in predicting the future. Only in an intermediate regime, where there are interesting non-random dynamics, should there be substantial uncertainty about VF(a) that can be reduced by knowing VP(a).

VP(a), VF(a)

VP(a)

+ H

VF(a)

As Shalizi et al. \[12\] point out, a major advantage of light-cone complexity, compared to sophistication, logical depth, and so on, is that light-cone complexity has a clear “operational meaning”:

7

it is easy to state the question that light-cone complexity is answering. That question is the following: “how much could I possibly predict about the configurations in a’s future, given complete information about a’s past?” The reason to focus on light-cones, rather than other sets of points, is that the light-cones are automatically determined once we know the causal structure: there seems to be little arbitrariness about them.

On the other hand, depending on the application, an obvious drawback of light-cone complexity is that it can’t tell us the “inherent” complexity of an object x, without knowing about x’s past and future. If we wanted to use a complexity measure to make inferences about x’s past and future, this might be seen as question-begging. A less obvious drawback arises if we consider a dynamical system that changes slowly with time: for example, a version of the coﬀee automaton where just a single cream particle is randomly moved at each time step. Consider such a system in its “late” stages: that is, after the coﬀee and cream have fully mixed. Even then, Shalizi et al.’s LCC (a) measure will remain large, but not for any “interesting” reason: only because a’s past light-cone will contain almost the same (random) information as its future light-cone, out to a very large distance! Thus, LCC seems to give an intuitively wrong answer in these cases (though no doubt one could address the problem by redefining LCC in some suitable way).

The computational situation for LCC seems neither better nor worse to us than that for (say) apparent complexity or resource-bounded sophistication. Since the light-cones P (a) and V (a) are formally infinite, a first step in estimating LCC (a)—as Shalizi et al. point out—is to impose some finite cutoﬀt on the number of steps into a’s past and future one is willing to look. Even then, one needs to estimate the mutual information I

between the truncated light-cones Pt (a) and Ft (a), a problem that na¨ıvely requires a number of samples exponential in t. One could address this problem by simply taking t extremely small (Shalizi et al. set t = 1). Alternatively, if a large t was needed, one could use the same Kolmogorov-complexity-based approach that we adopt in this paper for apparent complexity. That is, one first replaces the mutual information by the mutual algorithmic information

VPt(a) : VFt(a)

−K

K

VPt(a) : VFt(a)

= K

VPt(a)

+ K

VFt(a)

VPt(a), VFt(a)

, (8)

and then estimates K (x) using some computable proxy such as gzip file size.

---

Full document: [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](../../papers/25-coffee-automaton.md) · Page-level evidence: [paper-pages/25-coffee-automaton](../../paper-pages/25-coffee-automaton/index.md)
