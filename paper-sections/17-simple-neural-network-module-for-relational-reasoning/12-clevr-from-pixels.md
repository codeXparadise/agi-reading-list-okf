---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
source: ../../papers/17-simple-neural-network-module-for-relational-reasoning.md
paper_title: A Simple Neural Network Module for Relational Reasoning
sequence: 17
section: 5.1 CLEVR from pixels
section_role: other
section_index: 12
pages: [6]
topics: ["../../topics/relational-reasoning.md", "../../topics/graph-neural-networks.md"]
description: "Our model achieved state-of-the-art performance on CLEVR at 95.5%, exceeding the best model trained only on the pixel images and questions at the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5.1 CLEVR from pixels

> Section 12 of 22 from [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md) · `other` · pages 6-6

Our model achieved state-of-the-art performance on CLEVR at 95.5%, exceeding the best model trained only on the pixel images and questions at the time of the dataset’s publication by 27%, and surpassing human performance in the task (see Table 1 and Figure 3).

These results – in particular, those obtained in the compare attribute and count categories – are a testament to the ability of our model to do relational reasoning. In fact, it is in these categories that state-of-the-art models struggle most. Furthermore, the relative simplicity of the network components used in our model suggests that the diﬃculty of the CLEVR task lies in its relational reasoning demands, not on the language or the visual processing.

Results using privileged training information A more recent study reports overall performance of 96.9% on CLEVR, but uses additional supervisory signals on the functional programs used to generate the CLEVR questions \[16\]. It is not possible for us to directly compare this to our work since we do not use these additional supervision signals. Nonetheless, our approach greatly outperforms a version of their model that was not trained with these extra signals, and even versions of their model trained using 9K or 18K ground-truth programs. Thus, RNs can achieve very competitive, and even super-human results under much weaker and more natural assumptions, and even in situations when functional programs are unavailable.

---

Full document: [17 - A Simple Neural Network Module for Relational Reasoning](../../papers/17-simple-neural-network-module-for-relational-reasoning.md) · Page-level evidence: [paper-pages/17-simple-neural-network-module-for-relational-reasoning](../../paper-pages/17-simple-neural-network-module-for-relational-reasoning/index.md)
