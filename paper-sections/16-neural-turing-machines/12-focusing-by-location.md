---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/16-neural-turing-machines.md
source: ../../papers/16-neural-turing-machines.md
paper_title: Neural Turing Machines
sequence: 16
section: 3.3.2 Focusing by Location
section_role: other
section_index: 12
pages: [7, 8]
topics: ["../../topics/memory-augmented-networks.md", "../../topics/recurrent-neural-networks.md"]
description: "The location-based addressing mechanism is designed to facilitate both simple iteration across the locations of the memory and random-access jumps.…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.3.2 Focusing by Location

> Section 12 of 25 from [16 - Neural Turing Machines](../../papers/16-neural-turing-machines.md) · `other` · pages 7-8

The location-based addressing mechanism is designed to facilitate both simple iteration across the locations of the memory and random-access jumps. It does so by implementing a rotational shift of a weighting. For example, if the current weighting focuses entirely on a single location, a rotation of 1 would shift the focus to the next location. A negative shift would move the weighting in the opposite direction.

Prior to rotation, each head emits a scalar interpolation gate gt in the range (0, 1). The value of g is used to blend between the weighting wt−1 produced by the head at the previous time-step and the weighting wc

t produced by the content system at the current time-step, yielding the gated weighting wg

t :

wg

t ←−gtwc

t + (1 −gt)wt−1. (7)

If the gate is zero, then the content weighting is entirely ignored, and the weighting from the previous time step is used. Conversely, if the gate is one, the weighting from the previous iteration is ignored, and the system applies content-based addressing.

After interpolation, each head emits a shift weighting st that defines a normalised distribution over the allowed integer shifts. For example, if shifts between -1 and 1 are allowed, st has three elements corresponding to the degree to which shifts of -1, 0 and 1 are performed. The simplest way to define the shift weightings is to use a softmax layer of the appropriate size attached to the controller. We also experimented with another technique, where the controller emits a single scalar that is interpreted as the lower bound of a width one uniform distribution over shifts. For example, if the shift scalar is 6.7, then st(6) = 0.3, st(7) = 0.7, and the rest of st is zero.

8

If we index the N memory locations from 0 to N −1, the rotation applied to wg

t by st can be expressed as the following circular convolution:

N−1 X

wg

˜wt(i) ←−

t (j) st(i −j) (8)

j=0

where all index arithmetic is computed modulo N. The convolution operation in Equation (8) can cause leakage or dispersion of weightings over time if the shift weighting is not sharp. For example, if shifts of -1, 0 and 1 are given weights of 0.1, 0.8 and 0.1, the rotation will transform a weighting focused at a single point into one slightly blurred over three points. To combat this, each head emits one further scalar γt ≥1 whose effect is to sharpen the final weighting as follows:

wt(i) ←− ˜wt(i)γt P

j ˜wt(j)γt (9)

The combined addressing system of weighting interpolation and content and locationbased addressing can operate in three complementary modes. One, a weighting can be chosen by the content system without any modification by the location system. Two, a weighting produced by the content addressing system can be chosen and then shifted. This allows the focus to jump to a location next to, but not on, an address accessed by content; in computational terms this allows a head to find a contiguous block of data, then access a particular element within that block. Three, a weighting from the previous time step can be rotated without any input from the content-based addressing system. This allows the weighting to iterate through a sequence of addresses by advancing the same distance at each time-step.

---

Full document: [16 - Neural Turing Machines](../../papers/16-neural-turing-machines.md) · Page-level evidence: [paper-pages/16-neural-turing-machines](../../paper-pages/16-neural-turing-machines/index.md)
