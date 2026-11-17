---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md
source: ../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md
paper_title: The Unreasonable Effectiveness of Recurrent Neural Networks
sequence: 8
section: Shakespeare
section_role: other
section_index: 4
pages: []
topics: ["../../topics/recurrent-neural-networks.md"]
description: "It looks like we can learn to spell English words. But how about if there is more structure and style in the data? To examine this I downloaded all…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Shakespeare

> Section 4 of 10 from [08 - The Unreasonable Effectiveness of Recurrent Neural Networks](../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md) · `other` · pages n/a

It looks like we can learn to spell English words. But how about if there is more structure and style in the data? To examine this I downloaded all the works of Shakespeare and concatenated them into a single (4.4MB) file. We can now afford to train a larger network, in this case lets try a 3-layer RNN with 512 hidden nodes on each layer. After we train the network for a few hours we obtain samples such as:

```
PANDARUS:
Alas, I think he shall be come approached and the day
When little srain would be attain'd into being never fed,
And who is but a chain and subjects of his death,
I should not sleep.

Second Senator:
They are away this miseries, produced upon my soul,
Breaking and strongly should be buried, when I perish
The earth and thoughts of many states.

DUKE VINCENTIO:
Well, your wit is in the care of side and that.

Second Lord:
They would be ruled after this chamber, and
my fair nues begun out of the fact, to be conveyed,
Whose noble souls I'll have the heart of the wars.

Clown:
Come, sir, I will make did behold your worship.

VIOLA:
I'll drink it.
```

Remember, all the RNN knows are characters, so in particular it samples both speaker’s names and the contents. Sometimes we also get relatively extented monologue passages, such as:

```
VIOLA:
Why, Salisbury must find his flesh and thought
That which I am not aps, not a man and in fire,
To show the reining of the raven and the wars
To grace my hand reproach within, and not a fair are hand,
That Caesar and my goodly father's world;
When I was heaven of presence and our fleets,
We spare with hours, but cut thy council I am great,
Murdered and by thy master's ready there
My power to give thee but so much as hell:
Some service in the noble bondman here,
Would show him to her wine.

KING LEAR:
O, if you were a feeble sight, the courtesy of your law,
Your sight and several breath, will wear the gods
With his heads, and my hands are wonder'd at the deeds,
So drop upon your lordship's head, and your opinion
Shall be against your honour.
```

I can barely recognize these samples from actual Shakespeare :) If you like Shakespeare, you might appreciate this [100,000 character sample](http://cs.stanford.edu/people/karpathy/char-rnn/shakespear.txt). Of course, you can also generate an infinite amount of your own samples at different temperatures with the provided code.

---

Full document: [08 - The Unreasonable Effectiveness of Recurrent Neural Networks](../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md) · Page-level evidence: [paper-pages/08-unreasonable-effectiveness-of-recurrent-neural-networks](../../paper-pages/08-unreasonable-effectiveness-of-recurrent-neural-networks/index.md)
