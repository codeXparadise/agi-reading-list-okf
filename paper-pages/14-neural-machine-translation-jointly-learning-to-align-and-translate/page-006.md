---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md
source: ../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md
paper_title: Neural Machine Translation by Jointly Learning to Align and Translate
sequence: 14
page: 6
pages: [6]
page_of: 15
topics: ["../../topics/attention.md", "../../topics/machine-translation.md", "../../topics/sequence-to-sequence.md"]
description: "Table 1: BLEU scores of the trained models computed on the test set. The second and third columns show respectively the scores on all the sentences…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 6 of 15 - Neural Machine Translation by Jointly Learning to Align and Translate

> Page 6 of the source PDF, verbatim as extracted. Canonical document: [14 - Neural Machine Translation by Jointly Learning to Align and Translate](../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md)

Table 1: BLEU scores of the trained models computed on the test set. The second and third columns show respectively the scores on all the sentences and, on the sentences without any unknown word in themselves and in the reference translations. Note that RNNsearch-50⋆was trained much longer until the performance on the development set stopped improving. (◦) We disallowed the models to generate \[UNK\] tokens when only the sentences having no unknown words were evaluated (last column).

Model All No UNK◦

RNNencdec-30 13.93 24.19 RNNsearch-30 21.50 31.44 RNNencdec-50 17.82 26.71 RNNsearch-50 26.75 34.16 RNNsearch-50⋆ 28.45 36.15 Moses 33.30 35.63

5.2 QUALITATIVE ANALYSIS

5.2.1 ALIGNMENT

The proposed approach provides an intuitive way to inspect the (soft-)alignment between the words in a generated translation and those in a source sentence. This is done by visualizing the annotation weights αij from Eq. (6), as in Fig. 3. Each row of a matrix in each plot indicates the weights associated with the annotations. From this we see which positions in the source sentence were considered more important when generating the target word.

We can see from the alignments in Fig. 3 that the alignment of words between English and French is largely monotonic. We see strong weights along the diagonal of each matrix. However, we also observe a number of non-trivial, non-monotonic alignments. Adjectives and nouns are typically ordered differently between French and English, and we see an example in Fig. 3 (a). From this figure, we see that the model correctly translates a phrase \[European Economic Area\] into \[zone

´economique europ´een\]. The RNNsearch was able to correctly align \[zone\] with \[Area\], jumping over the two words (\[European\] and \[Economic\]), and then looked one word back at a time to complete the whole phrase \[zone ´economique europ´eenne\].

The strength of the soft-alignment, opposed to a hard-alignment, is evident, for instance, from Fig. 3 (d). Consider the source phrase \[the man\] which was translated into \[l’ homme\]. Any hard alignment will map \[the\] to \[l’\] and \[man\] to \[homme\]. This is not helpful for translation, as one must consider the word following \[the\] to determine whether it should be translated into \[le\], \[la\], \[les\] or \[l’\]. Our soft-alignment solves this issue naturally by letting the model look at both \[the\] and \[man\], and in this example, we see that the model was able to correctly translate \[the\] into \[l’\]. We observe similar behaviors in all the presented cases in Fig. 3. An additional benefit of the soft alignment is that it naturally deals with source and target phrases of different lengths, without requiring a counter-intuitive way of mapping some words to or from nowhere (\[NULL\]) (see, e.g., Chapters 4 and 5 of Koehn, 2010).

5.2.2 LONG SENTENCES

As clearly visible from Fig. 2 the proposed model (RNNsearch) is much better than the conventional model (RNNencdec) at translating long sentences. This is likely due to the fact that the RNNsearch does not require encoding a long sentence into a fixed-length vector perfectly, but only accurately encoding the parts of the input sentence that surround a particular word.

As an example, consider this source sentence from the test set:

An admitting privilege is the right of a doctor to admit a patient to a hospital or a medical centre to carry out a diagnosis or a procedure, based on his status as a health care worker at a hospital.

The RNNencdec-50 translated this sentence into:

Un privil\`ege d’admission est le droit d’un m´edecin de reconnaˆıtre un patient \`a l’hˆopital ou un centre m´edical d’un diagnostic ou de prendre un diagnostic en fonction de son ´etat de sant´e.

---

[previous page](page-005.md) · [next page](page-007.md) · [all pages](index.md)
