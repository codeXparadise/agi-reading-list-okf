---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 4. Universal Intelligence Measure
section_role: other
section_index: 36
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "“. . . we need a definition of intelligence that is applicable to machines as well as humans or even dogs. Further, it would be helpful to have a…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 4. Universal Intelligence Measure

> Section 36 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

“. . . we need a definition of intelligence that is applicable to machines as well as humans or even dogs. Further, it would be helpful
to have a relative measure of intelligence, that would enable us to
judge one program more or less intelligent than another, rather
than identify some absolute criterion. Then it will be possible to
assess whether progress is being made . . . ” Johnson (1992)

In Chapter 1 we explored the concept of intelligence and proposed an informal definition of intelligence. In Chapter 2 we introduced universal agents,
and in Chapter 3 we detailed some of the classes of environments in which
their behaviour converges to optimal. This shows that universal agents are
highly intelligent with respect to the definition of intelligence that we have
adopted. One could argue that the universal agent defined over the space of
all enumerable chronological environments, that is AIXI, is in some sense an
optimal machine intelligence.

In this chapter we turn this idea on its head: Instead of using the theory of
universal artificial intelligence to define powerful agents, we use it instead to
formally define intelligence itself. One approach is to take AIXI and to mathematically define a performance measure under which AIXI is the maximal
agent by construction. This is the approach taken by the Intelligence Order
Relation (see Section 5.1.4 in Hutter, 2005). Although this produces a very
general relation for comparing the relative performance of agents, in order to
justify calling this a formal definition of “intelligence” one must carefully examine the way in which intelligence is defined, and then show how this relates
to the equation.

In this chapter we bridge this gap by proceeding in the opposite direction.
We begin with our informal definition of intelligence from Chapter 1 that was
based on a range of standard definitions given by psychologists and artificial
intelligence researchers. We then formalise this definition, borrowing ideas
from reinforcement learning, Kolmogorov complexity, Solomonoff induction
and universal artificial intelligence theory as necessary. The result is an equation for intelligence that is strongly related to existing definitions, and with
respect to which highly intelligent agents can be proven to have powerful optimality properties. We then look at some of this definition’s properties and
compare it to other tests and definitions of machine intelligence.

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
