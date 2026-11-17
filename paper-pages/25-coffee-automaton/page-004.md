---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/25-coffee-automaton.md
source: ../../papers/25-coffee-automaton.md
paper_title: "Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton"
sequence: 25
page: 4
pages: [4]
page_of: 22
topics: ["../../topics/kolmogorov-complexity.md"]
description: "information in a string—while using Kolmogorov complexity itself to define what is meant by “nonrandom.” Given an n-bit string x, let a model for x…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 4 of 22 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton

> Page 4 of the source PDF, verbatim as extracted. Canonical document: [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](../../papers/25-coffee-automaton.md)

information in a string—while using Kolmogorov complexity itself to define what is meant by “nonrandom.” Given an n-bit string x, let a model for x be a set S ⊆{0, 1}n such that x ∈S. Let K (S) be the length of the shortest program that enumerates the elements of S, in any order (crucially, the program must halt when it is done enumerating the elements). Also, let K (x|S) be the length of the shortest program that outputs x given as input a description of x. Then we can consider x to be a “generic” element of S if K (x|S) ≥log2 |S| −c for some small constant c. This means intuitively that S is a “maximal” model for x: one can summarize all the interesting, non-random properties of x by simply saying that x ∈S.

Now the c-sophistication of x or sophc (x), defined by Koppel \[8\], is the minimum of K (S) over all models S for x such that K (S)+log2 |S| ≤K (x)+c. (The optimal such S is said to “witness” sophc (x).) In words, sophc (x) is the smallest possible amount of “non-random” information in a program for x that consists of two parts—a “non-random” part (specifying S) and a “random” part (specifying x within S)—assuming the program is also near-minimal. We observe the following:

(i) sophc (x) ≤K (x) + O (1), since we can always just take S = {x} as our model for x.

(ii) Most strings x satisfy sophc (x) = O (1), since we can take S = {0, 1}n as our model for x.

(iii) If S witnesses sophc (x), then log2 |S| ≤K (x) −K (S) + c ≤K (x|S) + c, meaning that x

must be a “generic” element of S.

It can be shown (see G´acs, Tromp, and Vit´anyi \[6\] or Antunes and Fortnow \[1\]) that there do exist highly “sophisticated” strings x, which satisfy sophc (x) ≥n −c −O (log n). Interestingly, the proof of that result makes essential use of the assumption that the program for S halts, after it has finished listing S’s elements. If we dropped that assumption, then we could always achieve K (S) = O (log n), by simply taking S to be the set of all y ∈{0, 1}n such that K (y) ≤K (x), and enumerating those y’s in a dovetailing fashion.

Recently, Mota et al. \[10\] studied a natural variant of sophistication, in which one only demands that S be a maximal model for x (i.e., that K (x|S) ≥log2 |S| −c), and not that S also lead to a near-optimal two-part program for x (i.e., that K (S)+log2 |S| ≤K (x)+c). More formally, Mota et al. define the na¨ıve c-sophistication of x, or nsophc (x), to be the minimum of K (S) over all models S for x such that K (x|S) ≥log2 |S|−c. By point (iii) above, it is clear that nsophc (x) ≤sophc (x). A priori, nsophc (x) could be much smaller sophc (x), thereby leading to two diﬀerent sophistication notions. However, it follows from an important 2004 result of Vereshchagin and Vit´anyi \[13\] that sophc+O(log n) (x) ≤nsophc (x) for all x, and hence the two notions are basically equivalent.

Sophistication is sometimes criticized for being “brittle”: it is known that increasing the parameter c only slightly can cause sophc (x) and nsophc (x) to fall drastically, say from n −O (log n) to O (1). However, a simple fix to that problem is to consider the quantities minc {c + sophc (x)} and minc {c + nsophc (x)}. Those are known, respectively, as the coarse sophistication csoph (x) and na¨ıve coarse sophistication ncsoph (x), and they satisfy ncsoph (x) ≤csoph (x) ≤ncsoph (x) + O (log n).

The advantage of sophistication is that it captures, more cleanly than any other measure, what exactly we mean by “interesting” versus “random” information. Unlike with apparent complexity, with sophistication there’s no need to specify a smoothing function f, with the arbitrariness that seems to entail. Instead, if one likes, the definition of sophistication picks out a smoothing function for us: namely, whatever function maps x to its corresponding model S.

5

---

[previous page](page-003.md) · [next page](page-005.md) · [all pages](index.md)
