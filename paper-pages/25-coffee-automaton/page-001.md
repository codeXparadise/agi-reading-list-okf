---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/25-coffee-automaton.md
source: ../../papers/25-coffee-automaton.md
paper_title: "Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton"
sequence: 25
page: 1
pages: [1]
page_of: 22
topics: ["../../topics/kolmogorov-complexity.md"]
description: "the liquids are mixed in some areas but not in others—it seems more diﬃcult to describe what the contents of the cup look like. Thus, it appears that…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 1 of 22 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton

> Page 1 of the source PDF, verbatim as extracted. Canonical document: [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](../../papers/25-coffee-automaton.md)

the liquids are mixed in some areas but not in others—it seems more diﬃcult to describe what the contents of the cup look like.

Thus, it appears that the coﬀee cup system starts out at a state of low complexity, and that the complexity first increases and then decreases over time. In fact, this rising-falling pattern of complexity seems to hold true for many closed systems. One example is the universe itself. The universe began near the Big Bang in a low-entropy, low-complexity state, characterized macroscopically as a smooth, hot, rapidly expanding plasma. It is predicted to end in the high-entropy, low-complexity state of heat death, after black holes have evaporated and the acceleration of the universe has dispersed all of the particles (about 10100 years from now). But in between, complex structures such as planets, stars, and galaxies have developed. There is no general principle that quantifies and explains the existence of high-complexity states at intermediate times in closed systems. It is the aim of this work to explore such a principle, both by developing a more formal definition of “complexity,” and by running numerical experiments to measure the complexity of a simulated coﬀee cup system. The idea that complexity first increases and then decreases in as entropy increases in closed system has been suggested informally \[4,7\], but as far as we know this is the first quantitative exploration of the phenomenon.

## 2 Background

Before discussing how to define “complexity,” let’s start with the simpler question of how to define entropy in a discrete dynamical system. There are various definitions of entropy that are useful in diﬀerent contexts. Physicists distinguish between the Boltzmann and Gibbs entropies of physical systems. (There is also the phenomenological thermodynamic entropy and the quantum-mechanical von Neumann entropy, neither of which are relevant here.) The Boltzmann entropy is an objective feature of a microstate, but depends on a choice of coarse-graining. We imagine coarse-graining the space of microstates into equivalence classes, so that each microstate xa is an element of a unique macrostate XA. The volume WA of the macrostate is just the number of associated microstates xa ∈XA. Then the Boltzmann entropy of a microstate xa is the normalized logarithm of the volume of the associated macrostate:

SBoltzmann(xa) := kB log WA, (1)

where kB is Boltzmann’s constant (which we can set equal to 1). The Boltzmann entropy is independent of our knowledge of the system; in particular, it can be nonzero even when we know the exact microstate. The Gibbs entropy (which was also studied by Boltzmann), in contrast, refers to a distribution function ρ(x) over the space of microstates, which can be thought of as characterizing our ignorance of the exact state of the system. It is given by

X

SGibbs\[ρ\] := −

ρ(x) log ρ(x). (2)

x

In probability theory, communications, information theory, and other areas, the Shannon entropy of a probability distribution D = (px)x is the expected number of random bits needed to output a sample from the distribution:

X

H(D) := −

px log px. (3)

x

2

---

first page · [next page](page-002.md) · [all pages](index.md)
