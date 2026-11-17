---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
source: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
paper_title: A Simple Neural Network Module for Relational Reasoning
sequence: 17
section: 3.4 Dynamic physical systems
section_role: other
section_index: 10
pages: [4]
topics: ["../../topics/relational-reasoning.md", "../../topics/graph-neural-networks.md"]
description: "We developed a dataset of simulated physical mass-spring systems using the MuJoCo physics engine [40]. Each scene contained 10 colored balls moving…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.4 Dynamic physical systems

> Section 10 of 22 from [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md) · `other` · pages 4-4

We developed a dataset of simulated physical mass-spring systems using the MuJoCo physics engine

\[40\]. Each scene contained 10 colored balls moving on a table-top surface. Some of the balls moved independently, free to collide with other balls and the barrier walls. Other randomly selected ball pairs were connected by invisible springs or a rigid constraint. These connections prevented the balls from moving independently, due to the force imposed through the connections. Input data consisted of state descriptions matrices, where each ball was represented as a row in a matrix with features representing the RGB color values of each object and their spatial coordinates (x, y) across 16 sequential time steps. The introduction of random links between balls created an evolving physical system with a variable number “systems” of connected balls (where “systems” refers to connected graphs with balls as nodes and connections between balls as edges). We defined two separate tasks: 1) infer the existence or absence of connections between balls when only observing their color and coordinate positions across multiple sequential frames, and 2) count the number of systems on the table-top, again when only observing each ball’s color and coordinate position across multiple sequential frames.

Both of these tasks involve reasoning about the relative positions and velocities of the balls to infer whether they are moving independently, or whether their movement is somehow dependent on the movement of other balls through invisible connections. For example, if the distance between two balls remains similar across frames, then it can be inferred that there is a connection between them. The first task makes these inferences explicit, while the second task demands that this reasoning occur implicitly, which is much more diﬃcult. For further information on all tasks, including videos of the dynamic systems, see the supplementary information.

---

Full document: [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md) · Page-level evidence: [paper-pages/17-simple-neural-network-module-for-relational-reasoning](../../paper-pages/17-simple-neural-network-module-for-relational-reasoning/index.md)
