---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
source: ../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md
paper_title: Kolmogorov Complexity and Algorithmic Randomness
sequence: 26
page: 54
pages: [54]
page_of: 79
topics: ["../../topics/kolmogorov-complexity.md", "../../topics/minimum-description-length.md"]
description: "2.2. CONDITIONAL COMPLEXITY 55 pawns at all); after a pawn is places, it cannot be moved or removed. Also Black can irreversibly mark some cells. The…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 54 of 79 - Kolmogorov Complexity and Algorithmic Randomness

> Page 54 of the source PDF, verbatim as extracted. Canonical document: [26 - Kolmogorov Complexity and Algorithmic Randomness](../../papers/26-kolmogorov-complexity-and-algorithmic-randomness.md)

2.2. CONDITIONAL COMPLEXITY 55
pawns at all); after a pawn is places, it cannot be moved or removed. Also Black
can irreversibly mark some cells. The players should obey the following restrictions:
(a) each of the players can place at most 2𝑖 pawns at row 𝑖 (the bottom row
has number 0, the upper row has number 𝑛 − 1);
(b) Black can mark at most half of the cells in each column.
A white pawn is declared as killed if its cell is marked or if there is a black
paws below it (in the same column). The game does not end formally (though it is
essentially a finite game); White wins if in the limit there is at least one non-killed
white pawn.
White has a winning strategy in this game: place a pawn in the top row and
wait until it is killed. If it is killed by the black pawn below, switch to the next
column (for example, White can go from left to right starting with the leftmost
column). If the pawn was killed by marking its cell, White places another pawn
just below the first one, etc. (We may assume that Black’s moves kill the white
pawn, all other moves can be postponed, since the winner is determined by the
limit position.) Recall that Black can mark at most half of the column, so Black
is forced to put some pawn in the column at some point. It cannot be done in all
columns, since the sum of 2𝑖 for all rows is less (by 1) than the width of the table.
Note also that White will not violate restrictions on the number of pawns in each
row, since in all the columns (except the currently active one) under each white
pawn (in row 𝑖) there is a black paws (in some row 𝑗 < 𝑖), and the sum of 2𝑗 for
all 𝑗 < 𝑖 is less that 2𝑖 and there is a space for one more white pawn.
After a winning strategy for White is described, consider the following “univer-
sal” strategy for Black: the cell (𝑥, 𝑖) is marked as soon as we find that 𝐶(𝑖 | 𝑥) <
log 𝑛 − 1; a black pawn in placed at (𝑥, 𝑖) when a conditional description of 𝑥
(given 𝑛) of length 𝑖 is found. It is easy to check that Black obeys the game rules.
White wins, and a live white pawn at the cell (𝑥, 𝑖) means that 𝐶(𝑥 | 𝑛) > 𝑖 and
𝐶(𝑖 | 𝑥) > log 𝑛−1. Since the actions of White (playing against computable strategy
of Black) are computable, we conclude that 𝐶(𝑥 | 𝑛) > 𝑖 + 𝑂(1): the set of white
pawns in row 𝑖 is enumerable and it contains at most 2𝑖 elements.
This argument shows that 𝐶(𝐶(𝑥 | 𝑛) | 𝑥) > log 𝑛 − 1 (not exactly what we
wanted); to get the desired result, we should change the game and consider in
paraller boards of all sizes.
46 Prove that for some constant 𝑐 for any string 𝑥 and for every number 𝑛
there exists a string 𝑦 of length 𝑛 such that
𝐶(𝑥𝑦) > 𝐶(𝑥 | 𝑛) + 𝑛 − 𝑐.
[Hint: For a given 𝑛 the number of strings 𝑥 such that 𝐶(𝑥𝑦) < 𝑘 for any 𝑦 of
length 𝑛, does not exceed 2𝑘/2𝑛, and this property is enumerable. So we can apply
Theorem 19 (p. 50).]
47 Let 𝑓 be a function with natural arguments and values. Assume that
𝑓 (𝑛) + 𝜀ℎ 6 𝑓 (𝑛 + ℎ) 6 𝑓 (𝑛) + (1 − 𝜀)ℎ
for some 𝜀 > 0 and for all 𝑛 and ℎ. Prove that there exist an infinite bit sequence
𝜔 whose 𝑛-bit prefix has complexity 𝑓 (𝑛) + 𝑂(1) for every 𝑛.
[Hint: let us add blocks of length ℎ where ℎ is large enough. Each new block
being added to 𝑛-bit prefix increases complexity by more than 𝑓 (𝑛 + ℎ) − 𝑓 (𝑛) or
by less than 𝑓 (𝑛 + ℎ) − 𝑓 (𝑛), depending on the current situation (whether we are

---

[previous page](page-053.md) · [next page](page-055.md) · [all pages](index.md)
