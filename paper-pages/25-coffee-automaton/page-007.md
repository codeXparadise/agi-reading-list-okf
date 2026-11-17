---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/25-coffee-automaton.md
source: ../../papers/25-coffee-automaton.md
paper_title: "Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton"
sequence: 25
page: 7
pages: [7]
page_of: 22
topics: ["../../topics/kolmogorov-complexity.md"]
description: "it is easy to state the question that light-cone complexity is answering. That question is the following: “how much could I possibly predict about…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 7 of 22 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton

> Page 7 of the source PDF, verbatim as extracted. Canonical document: [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](../../papers/25-coffee-automaton.md)

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

## 2.5 Synthesis

It seems like we have a bestiary of diﬀerent complexity notions. Fortunately, the four notions discussed above can all be related to each other; let us discuss how.

First, one can view apparent complexity as a kind of “resource-bounded” sophistication. To see this, let f be any smoothing function. Then K (f (x)), the Kolmogorov complexity of f (x), is essentially equal to K (Sf,x), where

Sf,x := {y : f (y) = f (x)} . (9)

Thus, if instead of minimizing over all models S for x that satisfy some condition, we consider only the particular model Sf,x above, then sophistication reduces to apparent complexity. Note that this argument establishes neither that apparent complexity is an upper bound on sophistication, nor that it’s a lower bound. Apparent complexity could be larger, if the minimization found some model S for x with K (S) ≪K (Sf,x). But conversely, sophistication could also be larger, if

8

---

[previous page](page-006.md) · [next page](page-008.md) · [all pages](index.md)
