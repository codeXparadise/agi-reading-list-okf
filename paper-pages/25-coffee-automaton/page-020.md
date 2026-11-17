---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/25-coffee-automaton.md
source: ../../papers/25-coffee-automaton.md
paper_title: "Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton"
sequence: 25
page: 20
pages: [20]
page_of: 22
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Now let B be an L × L square of pixels, located anywhere on the n × n grid. Let at (B) be the number of cream particles in B after t steps. Clearly X…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 20 of 22 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton

> Page 20 of the source PDF, verbatim as extracted. Canonical document: [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](../../papers/25-coffee-automaton.md)

Now let B be an L × L square of pixels, located anywhere on the n × n grid. Let at (B) be the number of cream particles in B after t steps. Clearly

X

at (B) =

at (x, y) . (11)

(x,y)∈B

So it follows from Claim 1 that E \[at (B)\] ≤L2.

Fix some constant G, say 10. Then call B “bad” if at (B) diﬀers from E \[at (B)\] by more than L2/G. Suppose that at some time step t, no B is bad. Also, suppose we form a coarse-grained image by coloring each B one of G shades of gray, depending on the value of

at (B) G

(12)

L2

(or we color B white if at (B) > L2). Then it’s clear that the resulting image will be correctable, by adjusting each color by ±1, to one where all the B’s within the same row are assigned the same color—and furthermore, that color is simply

E \[at (B)\] G

. (13)

L2

If this happens, though, then the Kolmogorov complexity of the coarse-grained image can be at most log2 (n) + log2 (t) + O (1). For once we’ve specified n and t, we can simply calculate the expected color for each B, and no color ever deviates from its expectation.

So our task reduces to upper-bounding the probability that B is bad. By a Chernoﬀbound, since at (B) is just a sum of independent, 0/1 random variables,

−E \[at (B)\] δ2

Pr \[|at (B) −E \[at (B)\]| > δ E \[at (B)\]\] < 2 exp

. (14)

3

Plugging in L2/G = δ E \[at (B)\], we get

|at (B) −E \[at (B)\]| > L2

− L4

Pr

< 2 exp

. (15)

3G2 E \[at (B)\]

G

Since E \[at (B)\] ≤L2 from above, this in turn is at most

−L2

2 exp 

. (16)

3G2

Now, provided we choose a coarse-grain size

3 ln (2n2) = Θ 

p

p

L ≫G

G

log n

, (17)

the above will be much less than 1/n2. In that case, it follows by the union bound that, at each time step t, with high probability none of the L × L squares B are bad (since there at most n2

such squares). This is what we wanted to show.

21

---

[previous page](page-019.md) · [next page](page-021.md) · [all pages](index.md)
