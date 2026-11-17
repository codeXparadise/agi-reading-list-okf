---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/25-coffee-automaton.md
source: ../../papers/25-coffee-automaton.md
paper_title: "Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton"
sequence: 25
section: 1 Introduction
section_role: introduction
section_index: 3
pages: [1]
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Imagine a cup of coﬀee into which cream has just been poured. At first, the coﬀee and cream are separated. Over time, the two liquids diﬀuse until…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 1 Introduction

> Section 3 of 21 from [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](../../papers/25-coffee-automaton.md) · `introduction` · pages 1-1

Imagine a cup of coﬀee into which cream has just been poured. At first, the coﬀee and cream are separated. Over time, the two liquids diﬀuse until they are completely mixed. If we consider the coﬀee cup a closed system, we can say that its entropy is increasing over time, in accordance with the second law of thermodynamics. At the beginning, when the liquids are completely separated, the system is in a highly ordered, low-entropy state. After time has passed and the liquids have completely mixed, all of the initial structure is lost; the system has high entropy.

Just as we can reason about the disorder of the coﬀee cup system, we can also consider its “complexity.” Informally, by complexity we mean the amount of information needed to describe everything “interesting” about the system. At first, when the cream has just been poured into the coﬀee, it is easy to describe the state of the cup: it contains a layer of cream on top of a layer of coﬀee. Similarly, it is easy to describe the state of the cup after the liquids have mixed: it contains a uniform mixture of cream and coﬀee. However, when the cup is in an intermediate state—where

∗MIT. Email: aaronson@csail.mit.edu. This material is based upon work supported by the National Science Foundation under Grant No. 0844626, as well as an NSF Waterman Award.

†Walter Burke Institute for Theoretical Physics, Caltech. Email: seancarroll@gmail.com. This research is funded in part by DOE grant DE-FG02-92ER40701, and by the Gordon and Betty Moore Foundation through Grant 776 to the Caltech Moore Center for Theoretical Cosmology and Physics.

‡This work was done while the author was a student at MIT. Email: louelle@alum.mit.edu.

1

the liquids are mixed in some areas but not in others—it seems more diﬃcult to describe what the contents of the cup look like.

Thus, it appears that the coﬀee cup system starts out at a state of low complexity, and that the complexity first increases and then decreases over time. In fact, this rising-falling pattern of complexity seems to hold true for many closed systems. One example is the universe itself. The universe began near the Big Bang in a low-entropy, low-complexity state, characterized macroscopically as a smooth, hot, rapidly expanding plasma. It is predicted to end in the high-entropy, low-complexity state of heat death, after black holes have evaporated and the acceleration of the universe has dispersed all of the particles (about 10100 years from now). But in between, complex structures such as planets, stars, and galaxies have developed. There is no general principle that quantifies and explains the existence of high-complexity states at intermediate times in closed systems. It is the aim of this work to explore such a principle, both by developing a more formal definition of “complexity,” and by running numerical experiments to measure the complexity of a simulated coﬀee cup system. The idea that complexity first increases and then decreases in as entropy increases in closed system has been suggested informally \[4,7\], but as far as we know this is the first quantitative exploration of the phenomenon.

---

Full document: [25 - Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton](../../papers/25-coffee-automaton.md) · Page-level evidence: [paper-pages/25-coffee-automaton](../../paper-pages/25-coffee-automaton/index.md)
