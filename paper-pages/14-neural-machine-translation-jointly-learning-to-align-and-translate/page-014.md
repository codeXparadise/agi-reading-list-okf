---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md
source: ../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md
paper_title: Neural Machine Translation by Jointly Learning to Align and Translate
sequence: 14
page: 14
pages: [14]
page_of: 15
topics: ["../../topics/attention.md", "../../topics/machine-translation.md", "../../topics/sequence-to-sequence.md"]
description: "normalized the L2-norm of the gradient of the cost function each time to be at most a predefined threshold of 1, when the norm was larger than the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 14 of 15 - Neural Machine Translation by Jointly Learning to Align and Translate

> Page 14 of the source PDF, verbatim as extracted. Canonical document: [14 - Neural Machine Translation by Jointly Learning to Align and Translate](../../papers/14-neural-machine-translation-jointly-learning-to-align-and-translate.md)

normalized the L2-norm of the gradient of the cost function each time to be at most a predefined threshold of 1, when the norm was larger than the threshold (Pascanu et al., 2013b). Each SGD update direction was computed with a minibatch of 80 sentences.

At each update our implementation requires time proportional to the length of the longest sentence in a minibatch. Hence, to minimize the waste of computation, before every 20-th update, we retrieved 1600 sentence pairs, sorted them according to the lengths and split them into 20 minibatches. The training data was shuffled once before training and was traversed sequentially in this manner.

In Tables 2 we present the statistics related to training all the models used in the experiments.

## C TRANSLATIONS OF LONG SENTENCES

Source An admitting privilege is the right of a doctor to admit a patient to a hospital or a medical centre to carry out a diagnosis or a procedure, based on his status as a health care worker at a hospital. Reference Le privil\`ege d’admission est le droit d’un m´edecin, en vertu de son statut de membre soignant d’un hˆopital, d’admettre un patient dans un hˆopital ou un centre m´edical afin d’y d´elivrer un diagnostic ou un traitement. RNNenc-50 Un privil\`ege d’admission est le droit d’un m´edecin de reconnaˆıtre un patient \`a l’hˆopital ou un centre m´edical d’un diagnostic ou de prendre un diagnostic en fonction de son ´etat de sant´e. RNNsearch-50 Un privil\`ege d’admission est le droit d’un m´edecin d’admettre un patient \`a un hˆopital ou un centre m´edical pour effectuer un diagnostic ou une proc´edure, selon son statut de travailleur des soins de sant´e \`a l’hˆopital. Google Translate

Un privil\`ege admettre est le droit d’un m´edecin d’admettre un patient dans un hˆopital ou un centre m´edical pour effectuer un diagnostic ou une proc´edure, fond´ee sur sa situation en tant que travailleur de soins de sant´e dans un hˆopital.

Source This kind of experience is part of Disney’s efforts to ”extend the lifetime of its series and build new relationships with audiences via digital platforms that are becoming ever more important,” he added. Reference Ce type d’exp´erience entre dans le cadre des efforts de Disney pour ”´etendre la dur´ee de vie de ses s´eries et construire de nouvelles relations avec son public grˆace \`a des plateformes num´eriques qui sont de plus en plus importantes”, a-t-il ajout´e. RNNenc-50 Ce type d’exp´erience fait partie des initiatives du Disney pour ”prolonger la dur´ee de vie de ses nouvelles et de d´evelopper des liens avec les lecteurs num´eriques qui deviennent plus complexes. RNNsearch-50 Ce genre d’exp´erience fait partie des efforts de Disney pour ”prolonger la dur´ee de vie de ses s´eries et cr´eer de nouvelles relations avec des publics via des plateformes num´eriques de plus en plus importantes”, a-t-il ajout´e. Google Translate

Ce genre d’exp´erience fait partie des efforts de Disney \`a “´etendre la dur´ee de vie de sa s´erie et construire de nouvelles relations avec le public par le biais des plates-formes num´eriques qui deviennent de plus en plus important”, at-il ajout´e.

Source In a press conference on Thursday, Mr Blair stated that there was nothing in this video that might constitute a ”reasonable motive” that could lead to criminal charges being brought against the mayor. Reference En conf´erence de presse, jeudi, M. Blair a affirm´e qu’il n’y avait rien dans cette vid´eo qui puisse constituer des ”motifs raisonnables” pouvant mener au d´epˆot d’une accusation criminelle contre le maire. RNNenc-50 Lors de la conf´erence de presse de jeudi, M. Blair a dit qu’il n’y avait rien dans cette vid´eo qui pourrait constituer une ”motivation raisonnable” pouvant entraˆıner des accusations criminelles port´ees contre le maire. RNNsearch-50 Lors d’une conf´erence de presse jeudi, M. Blair a d´eclar´e qu’il n’y avait rien dans cette vid´eo qui pourrait constituer un ”motif raisonnable” qui pourrait conduire \`a des accusations criminelles contre le maire. Google Translate

Lors d’une conf´erence de presse jeudi, M. Blair a d´eclar´e qu’il n’y avait rien dans cette vido qui pourrait constituer un ”motif raisonnable” qui pourrait mener \`a des accusations criminelles portes contre le maire.

Table 3: The translations generated by RNNenc-50 and RNNsearch-50 from long source sentences (30 words or more) selected from the test set. For each source sentence, we also show the goldstandard translation. The translations by Google Translate were made on 27 August 2014.

---

[previous page](page-013.md) · [next page](page-015.md) · [all pages](index.md)
