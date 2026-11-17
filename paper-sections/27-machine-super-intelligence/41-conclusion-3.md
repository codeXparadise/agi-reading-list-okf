---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 4.5. Conclusion
section_role: conclusion
section_index: 41
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Given the obvious significance of formal definitions of intelligence for research, and calls for more direct measures of machine intelligence to…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 4.5. Conclusion

> Section 41 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `conclusion` · pages n/a

Given the obvious significance of formal definitions of intelligence for research,
and calls for more direct measures of machine intelligence to replace the problematic Turing test and other imitation based tests (Johnson, 1992), little work
has been done in this area. In this chapter we have attempted to tackle this
problem by taking an informal definition of intelligence modelled on expert
definitions of human intelligence, and then formalising it. We believe that the
resulting mathematical definition captures the concept of machine intelligence
in a very powerful and elegant way. Furthermore, we have seen that agents
which are extremely intelligent with respect to this definition, such as AIXI,
can be proven to have powerful optimality properties.

The central challenge for future work on universal intelligence is to convert
this theoretical definition of machine intelligence into a workable test. The
basic structure of such a test is already apparent from the equation for Υ: the
test would work by evaluating the performance of an agent on a large sample
of simulated environments, and then combine the agent’s performance in each
environment into an overall intelligence value. This would be done by weighting the agent’s performance in each environment according the environment’s
complexity.

A theoretical challenge that will need to be dealt with is to find a suitable
replacement for the incomputable Kolmogorov complexity function. One solution could be to use Kt complexity (Levin, 1973), another might be to use
the Speed prior (Schmidhuber, 2002). Both of these consider the complexity
of an algorithm to be determined by both its minimal description length and
running time, thus forcing the complexity measures to be computable. Taking
computation time into account also makes reasonable intuitive sense because
we would not usually consider a very short algorithm that takes an enormous
amount of time to run to be a particularly simple one. The fact that such an
approach can be made to work is evidenced by the C-Test (see Section 1.7).

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
