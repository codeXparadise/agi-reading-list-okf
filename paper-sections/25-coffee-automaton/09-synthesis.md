---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/25-coffee-automaton.md
source: ../../papers/25-coffee-automaton.md
paper_title: "Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton"
sequence: 25
section: 2.5 Synthesis
section_role: other
section_index: 9
pages: [7, 8, 9]
topics: ["../../topics/kolmogorov-complexity.md"]
description: "It seems like we have a bestiary of diﬀerent complexity notions. Fortunately, the four notions discussed above can all be related to each other; let…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 2.5 Synthesis

> Section 9 of 21 from [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](../../papers/25-coffee-automaton.md) · `other` · pages 7-9

It seems like we have a bestiary of diﬀerent complexity notions. Fortunately, the four notions discussed above can all be related to each other; let us discuss how.

First, one can view apparent complexity as a kind of “resource-bounded” sophistication. To see this, let f be any smoothing function. Then K (f (x)), the Kolmogorov complexity of f (x), is essentially equal to K (Sf,x), where

Sf,x := {y : f (y) = f (x)} . (9)

Thus, if instead of minimizing over all models S for x that satisfy some condition, we consider only the particular model Sf,x above, then sophistication reduces to apparent complexity. Note that this argument establishes neither that apparent complexity is an upper bound on sophistication, nor that it’s a lower bound. Apparent complexity could be larger, if the minimization found some model S for x with K (S) ≪K (Sf,x). But conversely, sophistication could also be larger, if

8

the model Sf,x happened to satisfy K (x|Sf,x) ≪log2 |Sf,x| (that is, x was a highly “non-generic” element of Sf,x).

Second, Antunes and Fortnow \[1\] proved a close relation between coarse sophistication and a version of logical depth. Specifically, the Busy Beaver function, BB (k), is defined as the maximum number of steps for which a k-bit program can run before halting when given a blank input. Then given a string x, Antunes and Fortnow \[1\] define the Busy Beaver computational depth depthBB (x) to be the minimum, over all programs p that output a model S for x in BB (k) steps or fewer, of |p| + k −K (x). They then prove the striking result that csoph and depthBB are essentially equivalent: for all x ∈{0, 1}n,

|csoph (x) −depthBB (x)| = O (log n) . (10)

Third, while light-cone complexity is rather diﬀerent from the other three measures (due to its taking as input an entire causal history), it can be loosely related to apparent complexity as follows. If LCC (a) is large, then the region around a must contain large “contingent structures”: structures that are useful for predicting future evolution, but that might have been diﬀerent in a diﬀerent run of the automaton. And one might expect those structures to lead to a large apparent complexity in a’s vicinity. Conversely, if the apparent complexity is large, then one expects contingent structures (such as milk tendrils, in the coﬀee automaton), which could then lead to nontrivial mutual information between a’s past and future light-cones.

Having described four complexity measures, their advantages and disadvantages, and their relationships to each other, we now face the question of which measure to use for our experiment. While it would be interesting to study the rise and fall of light-cone complexity in future work, here we decided to restrict ourselves to complexity measures that are functions of the current state. That leaves apparent complexity, sophistication, and logical depth (and various approximations, resource-bounded versions, and hybrids thereof).

Ultimately, we decided on a type of apparent complexity. Our reason was simple: because even after allowing resource bounds, we did not know of any eﬃcient way to approximate sophistication or logical depth. In more detail, given a bitmap image x of a coﬀee cup, our approach first “smears x out” using a smoothing function f, then uses the gzip file size of f (x) as an upper bound on the Kolmogorov complexity K (f (x)) (which, in turn, is a proxy for the Shannon entropy H (f (x)) of f (x) considered as a random variable). There are a few technical problems that arise when implementing this approach (notably, the problem of “border pixel artifacts”). We discuss those problems and our solutions to them in Section 4.

Happily, as discussed earlier in this section, our apparent complexity measure can be related to the other measures. For example, apparent complexity can be seen as an extremely resourcebounded variant of sophistication, with the set Sf,x of equation (9) playing the role of the model S. As discussed in Section 2.1, one might object to our apparent complexity measure on the grounds that our smoothing function f is “arbitrary,” that we had no principled reason to choose it rather than some other function. Interestingly, though, one can answer that objection by taking inspiration from light-cone complexity. Our smoothing function f will not be completely arbitrary, for the simple reason that the regions over which we coarse-grain—namely, squares of contiguous cells—will correspond to the coﬀee automaton’s causal structure.3

3Technically, if we wanted to follow the causal structure, then we should have used diamonds of continguous cells rather than squares. But this diﬀerence is presumably insignificant.

9

---

Full document: [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](../../papers/25-coffee-automaton.md) · Page-level evidence: [paper-pages/25-coffee-automaton](../../paper-pages/25-coffee-automaton/index.md)
