---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/16-neural-turing-machines.md
source: ../../papers/16-neural-turing-machines.md
paper_title: Neural Turing Machines
sequence: 16
page: 2
pages: [2]
page_of: 26
topics: ["../../topics/memory-augmented-networks.md", "../../topics/recurrent-neural-networks.md"]
description: "ical experiments involve recording from a single neuron or group of neurons in prefrontal cortex while a monkey is performing a task that involves…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 2 of 26 - Neural Turing Machines

> Page 2 of the source PDF, verbatim as extracted. Canonical document: [16 - Neural Turing Machines](../../papers/16-neural-turing-machines.md)

ical experiments involve recording from a single neuron or group of neurons in prefrontal cortex while a monkey is performing a task that involves observing a transient cue, waiting through a “delay period,” then responding in a manner dependent on the cue. Certain tasks elicit persistent firing from individual neurons during the delay period or more complicated neural dynamics. A recent study quantified delay period activity in prefrontal cortex for a complex, context-dependent task based on measures of “dimensionality” of the population code and showed that it predicted memory performance (Rigotti et al., 2013).

Modeling studies of working memory range from those that consider how biophysical circuits could implement persistent neuronal firing (Wang, 1999) to those that try to solve explicit tasks (Hazy et al., 2006) (Dayan, 2008) (Eliasmith, 2013). Of these, Hazy et al.’s model is the most relevant to our work, as it is itself analogous to the Long Short-Term Memory architecture, which we have modified ourselves. As in our architecture, Hazy et al.’s has mechanisms to gate information into memory slots, which they use to solve a memory task constructed of nested rules. In contrast to our work, the authors include no sophisticated notion of memory addressing, which limits the system to storage and recall of relatively simple, atomic data. Addressing, fundamental to our work, is usually left out from computational models in neuroscience, though it deserves to be mentioned that Gallistel and King (Gallistel and King, 2009) and Marcus (Marcus, 2003) have argued that addressing must be implicated in the operation of the brain.

## 2.2 Cognitive Science and Linguistics

Historically, cognitive science and linguistics emerged as fields at roughly the same time as artificial intelligence, all deeply influenced by the advent of the computer (Chomsky, 1956) (Miller, 2003). Their intentions were to explain human mental behaviour based on information or symbol-processing metaphors. In the early 1980s, both fields considered recursive or procedural (rule-based) symbol-processing to be the highest mark of cognition. The Parallel Distributed Processing (PDP) or connectionist revolution cast aside the symbol-processing metaphor in favour of a so-called “sub-symbolic” description of thought processes (Rumelhart et al., 1986).

Fodor and Pylyshyn (Fodor and Pylyshyn, 1988) famously made two barbed claims about the limitations of neural networks for cognitive modeling. They first objected that connectionist theories were incapable of variable-binding, or the assignment of a particular datum to a particular slot in a data structure. In language, variable-binding is ubiquitous; for example, when one produces or interprets a sentence of the form, “Mary spoke to John,” one has assigned “Mary” the role of subject, “John” the role of object, and “spoke to” the role of the transitive verb. Fodor and Pylyshyn also argued that neural networks with fixedlength input domains could not reproduce human capabilities in tasks that involve processing variable-length structures. In response to this criticism, neural network researchers including Hinton (Hinton, 1986), Smolensky (Smolensky, 1990), Touretzky (Touretzky, 1990), Pollack (Pollack, 1990), Plate (Plate, 2003), and Kanerva (Kanerva, 2009) investigated specific mechanisms that could support both variable-binding and variable-length

3

---

[previous page](page-001.md) · [next page](page-003.md) · [all pages](index.md)
