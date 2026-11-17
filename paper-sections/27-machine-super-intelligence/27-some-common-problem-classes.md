---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/27-machine-super-intelligence.md
source: ../../papers/27-machine-super-intelligence.md
paper_title: Machine Super Intelligence
sequence: 27
section: 3.3. Some common problem classes
section_role: other
section_index: 27
pages: []
topics: ["../../topics/kolmogorov-complexity.md"]
description: "Many of the problems considered in artificial intelligence can be expressed as classes of environments using our measure notation. In this section we…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 3.3. Some common problem classes

> Section 27 of 59 from [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · `other` · pages n/a

Many of the problems considered in artificial intelligence can be expressed as
classes of environments using our measure notation. In this section we will
formalise some of them.

3.3.1 Definition. A Function Maximisation Problem is an environment
(A, X,µ) such that O = R and for some objective function f : A→R we have
∀ax1:k,
{

$$
\left(\mathcal{A},\bar{\mathcal{X}},\mu\right)
$$

$$
\mathcal{O}=\mathcal{R}
$$

$$
f:\mathcal{A}\to\mathcal{R}
$$

$$
\forall ax_{1:k}
$$

$$
\mu(a x_{<k}a\underline{{x}}_{k}):=\left\{\begin{array}{l l}{1}&{\mathrm{i f~}o_{k}=f\big(a_{k}\big)\wedge r_{k}=\operatorname*{m a x}\{o_{1},\ldots,o_{k}\},}\\ {0}&{\mathrm{o t h e r w i s e.}}\end{array}\right.
$$

Essentially, the agent’s actions are interpreted as input to some function,
and in each cycle the result of the function is returned as an observation. We
do not simply return the current value of the function as the reward as this discourages the agent from exploring once a good value has been found. Rather we return the reward associated with the best value found so far. Obviously,
maximisation problems with different ranges, or minimisation problems, can
be expressed by applying a simple transformation to the original objective
function. For more on how AIXI deals with various types of function optimisation problems see Section 6.4 of (Hutter, 2005).

3.3.2 Example. Let f (a) := 1 − (a − 41)2. To maximise reward the agent
must generate the action that maximises f, that is, a = 41.

$$
f(a):=1-(a-\frac{1}{4})^2
$$

$$
a=\frac{1}{4}
$$

Artificial intelligence often considers environments that consist of some kind
of a game that is repetitively played by the agent. Games such as chess, various
card games, tic-tac-toe and others belong to this class, so long as at the end
of each match a new match is started. This can be formalised as follows:

3.3.3 Definition. A Repeated Strategic Game is an environment
(A, X,µ) where ∃l ∈ N such that ∀ax1:k,

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\exists l\in\mathbb{N}
$$

$$
\forall a x_{1:k}
$$

$$
\mu(ax_{<k}o\underline{x}_{k})=\mu(oo_{lm:k-1}o\underline{x}_{k})
$$

where m := ⌊k/l⌋ is the number of the episode when in cycle k, and l is the
episode length.

$$
m:=\left\lfloor k/l\right\rfloor
$$

Clearly, Bernoulli schemes and bandits are repeated strategic games. If we
want to allow games to finish before the episode finishes we can pad the remaining cycles, and perhaps also reward the system for padded cycles following
a victory in order to encourage rapid wins. For more on how AIXI deals with
strategic games see Section 6.3 of (Hutter, 2005).

Another common type of problem considered in artificial intelligence is classification. A classification problem consists of a domain space W and a set of
classes Z and some function f : W →Z. The agent must try to learn this
mapping based on examples. When given cases where the class is missing it
has to correctly guess the class in order to obtain reward. More formally:

$$
f:\mathcal{W}\to\mathcal{Z}
$$

3.3.4 Definition. A Classification Problem is an environment (A, X,µ)
set up as follows. Let W and Z be two sets called the attribute space
and the class space respectively. Z includes a special symbol “?” used to
indicate whether the agent needs to guess the class. Let O⊂W×Z and let
f : W→Z\{“?”} where ∀ax1:k such that xk−1 = wzrk−1 and xk = wzrk,

$$
\left(\mathcal{A},\mathcal{X},\mu\right)
$$

$$
\mathcal{Z}
$$

$$
\mathcal{O}\subset\mathcal{W}\times\mathcal{Z}
$$

$$
f:\mathcal{W}\to\mathcal{Z}\setminus\{``?\}
$$

$$
x_{k-1}=w z r_{k-1}
$$

$$
\forall a x_{1:k}
$$

$$
x_{k}=w z r_{k}
$$

$$
\mu(a x_{\leq k}a\underline{w}_{k})=\mu(\underline{w}_{k}),
$$

and for α ∈ (0, 1),

$$
\alpha\in(0,1)
$$

$$
\mu(w_{\underline{z}_{k}})=\left\{\begin{array}{ll}\alpha&if z_{k}=f(w_{k}),\\1-\alpha&if z_{k}=``?,\\0&otherwise,\end{array}\right.
$$

3. Taxonomy of Environments

and

$$
\mu(z_{k-1}a_{k}\underline{r}_{k})=\left\{\begin{array}{ll}1&z_{k-1}="?"\land a_{k}=f(w_{k-1})\land r_{k}=1,\\ 1&z_{k-1}\neq"?"\land r_{k}=0,\\ 0&otherwise.\end{array}\right.
$$

The first condition says that the distribution of the points in the attribute
space is independent of the system’s history. In other words, this part of xk is
a Bernoulli scheme. The second condition says that in each cycle the system
must either provide a training instance or ask for the agent to classify based on
the attribute vector. The parameter α controls how often the agent is asked
to guess the class. The third condition says that reward is given when the
system asks for a classification and the agent guesses it correctly. It is easy to
see that classification problems are passive MDPs.

$$
x_{k}
$$

3.3.5 Example. Let each element of W be a vector of medical measurements
for a patient, and Z some list of diseases. When provided with a list of
patients’ statistics and their diseases, the agent’s job is to learn a function
that determines which disease is present given a patient’s medical data.

For more on how AIXI deals with supervised learning problems see Section 6.5 of (Hutter, 2005).

---

Full document: [27 - Machine Super Intelligence](../../papers/27-machine-super-intelligence.md) · Page-level evidence: [paper-pages/27-machine-super-intelligence](../../paper-pages/27-machine-super-intelligence/index.md)
