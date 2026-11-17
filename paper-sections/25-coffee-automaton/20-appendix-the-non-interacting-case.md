---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/25-coffee-automaton.md
source: ../../papers/25-coffee-automaton.md
paper_title: "Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton"
sequence: 25
section: "9 Appendix: The Non-Interacting Case"
section_role: appendix
section_index: 20
pages: [19, 20, 21]
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Let’s consider the non-interacting coﬀee automaton on an n × n grid with periodic boundary conditions. At each time step, each cream particle moves…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 9 Appendix: The Non-Interacting Case

> Section 20 of 21 from [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](../../papers/25-coffee-automaton.md) · `appendix` · pages 19-21

Let’s consider the non-interacting coﬀee automaton on an n × n grid with periodic boundary conditions. At each time step, each cream particle moves to one of the 4 neighboring pixels uniformly at random. Let at (x, y) be the number of cream particles at point (x, y) after t steps.

Claim 1. For all x, y, t, we have E \[at (x, y)\] ≤1.

Proof. By induction on t. If t = 0, then a0 (x, y) ∈{0, 1}. Furthermore, by linearity of expectation,

E \[at+1 (x, y)\] = E \[at (x −1, y)\] + E \[at (x + 1, y)\] + E \[at (x, y −1)\] + E \[at (x, y + 1)\]

4 .

20

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

Full document: [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](../../papers/25-coffee-automaton.md) · Page-level evidence: [paper-pages/25-coffee-automaton](../../paper-pages/25-coffee-automaton/index.md)
