---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 5.7. Conclusion
section_role: conclusion
section_index: 50
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "We have shown that there does not exist an elegant constructive theory of prediction for computable sequences, even if we assume unbounded…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 5.7. Conclusion

> Section 50 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `conclusion` · pages n/a

We have shown that there does not exist an elegant constructive theory of
prediction for computable sequences, even if we assume unbounded computational resources, unbounded data and learning time, and place moderate
bounds on the Kolmogorov complexity of the sequences to be predicted. Very
powerful computable predictors are therefore necessarily complex. We have
further shown that the source of this problem is the existence of computable
sequences which are extremely expensive to compute. While we have proven
that very powerful prediction algorithms which can learn to predict these sequences exist, we have also proven that, unfortunately, mathematical analysis
cannot be used to discover these algorithms due to G¨odel incompleteness.

These results can be extended to more general settings, specifically to those
problems which are equivalent to, or depend on, sequence prediction. Consider,
for example, a reinforcement learning agent interacting with an environment,
as described in Chapters 2 and 3. In each interaction cycle the agent must
choose its actions so as to maximise the future rewards that it receives from
the environment. Of course the agent cannot know for certain if some action
will lead to rewards in the future. Whether explicitly or implicitly, it must
somehow predict these. Thus, at the heart of reinforcement learning lies a
prediction problem, and so the results for computable predictors presented in
this paper also apply to computable reinforcement learners. More specifically,
from Theorem 5.3.3 it follows that very powerful computable reinforcement
learners are necessarily complex, and from Theorem 5.6.1 it follows that it is
impossible to discover any of these extremely powerful reinforcement learning
algorithms mathematically. These relationships are illustrated in Figure 5.1.

It is reasonable to ask whether the assumptions we have made in our model
need to be changed. If we increase the power of the predictors further, for
example by providing them with some kind of an oracle, this would make the
predictors even more unrealistic than they currently are. This goes against
our goal of finding an elegant, powerful and general prediction theory that is
more realistic in its assumptions than Solomonoff’s incomputable model. On
the other hand, if we weaken our assumptions about the predictors’ resources
to make them more realistic, we are in effect taking a subset of our current
class of predictors. As such, all the same limitations and problems will still
apply, as well as some new ones.

It seems then that the way forward is to further restrict the problem space.
One possibility would be to bound the amount of computation time needed to
generate the next symbol in the sequence. However, if we do this without re- stricting the predictors’ resources then the simple predictor from Lemma 5.5.2
easily learns to predict any such sequence and thus the problem of prediction
in the limit has become trivial. Another possibility might be to bound the
memory of the machine used to generate the sequence, however this makes the
generator a finite state machine and thus bounds its computation time, again
making the problem trivial.

Perhaps the only reasonable solution would be to add additional restrictions
to both the algorithms which generate the sequences to be predicted, and to
the predictors. We may also want to consider not just learnability in the limit,
but also how quickly the predictor is able to learn. Of course we are then
facing a much more difficult analysis problem.

Powerful AI

Impossible Algorithms

Powerful but unprovable algorithms

Upper bound on performance of provable algorithms

Gödel Incompleteness

Weak provable algorithms

Weak AI

Simple Algorithms

Complex Algorithms

Figure 5.1.: Theorem 5.3.3 rules out simple but powerful artificial intelligence
algorithms, as indicated by the greyed out region in the upper
left. Theorem 5.6.1 upper bounds how powerful an algorithm can
be before it can no longer be proven to be a powerful algorithm.
This is indicated by the horizontal line separating the region of
provable algorithms from the region of G¨odel incompleteness.

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
