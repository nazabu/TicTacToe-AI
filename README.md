# Tic-Tac-Toe AI

An unbeatable Tic-Tac-Toe bot. The AI uses the **Minimax algorithm with Alpha-Beta Pruning** to play perfectly. It **never loses**. The best any opponent can achieve is a draw.

## How to Play

```bash
python main.py
```

Choose a mode:
- **Mode 1 — vs AI**: Play against the bot. Pick X (go first) or O (go second).
- **Mode 2 — vs Human**: Two players share the keyboard.

The board positions are numbered 0–8:

```
 0 | 1 | 2
-----------
 3 | 4 | 5
-----------
 6 | 7 | 8
```

Enter the number of the cell you want to claim.

## Project Structure

| File | Purpose |
|------|---------|
| `main.py` | Game loop, mode selection, turn management |
| `board.py` | Board creation, display, win detection, move helpers |
| `ai.py` | Minimax engine with alpha-beta pruning |
| `player.py` | Human input and validation |

---

## The Mathematics Behind the AI

### 1. Tic-Tac-Toe as a Finite, Deterministic, Perfect-Information Game

Tic-Tac-Toe belongs to the class of **combinatorial games**: two players alternate turns, both players see the full board state, there is no element of chance, and the game must end in finitely many moves.

These properties guarantee that a **game tree** — a rooted tree of every possible sequence of moves — is finite and fully enumerable. The upper bound on board states is 9! = 362,880 (the number of ways to fill 9 cells in sequence), though symmetry and early termination reduce the actually reachable states to 5,478 unique positions.

Because the game tree is finite and fully observable, a theorem from combinatorial game theory (proved by Zermelo in 1913) tells us:

> **Zermelo's Theorem**: In any finite two-player game of perfect information, either the first player has a winning strategy, the second player has a winning strategy, or both players can force a draw.

For Tic-Tac-Toe, exhaustive computation shows that **both players can force a draw**. Neither side has a forced win from the starting position. This means an optimal bot guarantees *at least* a tie and wins whenever the opponent deviates from optimal play.

### 2. The Minimax Algorithm

Minimax is the standard algorithm for finding optimal play in two-player zero-sum games. The idea:

- One player (the **maximiser**, our AI) tries to **maximise** the game's evaluation score.
- The other player (the **minimiser**, the human) tries to **minimise** it.
- At every game state, we assume both players play optimally.

#### Formal Definition

Let `V(s)` be the minimax value of a game state `s`:

```
           ┌  +W        if s is a terminal state where AI wins
           │  −W        if s is a terminal state where human wins
V(s)   =   │   0        if s is a terminal draw
           │  max { V(s') : s' ∈ children(s) }   if it is AI's turn
           └  min { V(s') : s' ∈ children(s) }   if it is human's turn
```

Where `W` is a positive constant (we use 100). The AI picks the child of the current state with the highest `V`; the human (from the AI's perspective) picks the child with the lowest `V`.

#### Depth Adjustment

A subtlety: if multiple moves all lead to a win, we want the AI to pick the **fastest** win. If multiple moves all lead to a loss, we want it to pick the **slowest** loss (giving the opponent more chances to err). We achieve this by adjusting the score with the search depth `d`:

```
Win  score = +W − d     (shallower wins score higher)
Loss score = −W + d     (deeper losses score less negative, i.e., "better")
```

For example, a win in 3 moves scores 97, while a win in 5 moves scores 95 — the AI prefers the quicker victory.

### 3. Alpha-Beta Pruning

Plain minimax explores every node in the game tree. Alpha-beta pruning produces the **exact same result** but skips branches that provably cannot affect the final decision.

#### How It Works

We maintain two values during the search:

- **α (alpha)**: the best score the **maximiser** (AI) can guarantee so far on any path from the root to the current node. Starts at −∞.
- **β (beta)**: the best score the **minimiser** (human) can guarantee so far. Starts at +∞.

The key insight is:

> If at any point **β ≤ α**, the current branch can be **pruned** (skipped) because the minimiser already has a better-or-equal option elsewhere and will never allow the game to reach this branch.

Specifically:
- **At a maximiser node**: after evaluating a child, update α = max(α, child_value). If β ≤ α, prune remaining children (**beta cutoff**).
- **At a minimiser node**: after evaluating a child, update β = min(β, child_value). If β ≤ α, prune remaining children (**alpha cutoff**).

#### Pruning Example

Consider this partial game tree (AI is maximiser):

```
            MAX
          /     \
       MIN       MIN
      / | \       |
     3  5  2      ?
```

At the left MIN node, after seeing children 3, 5, 2, MIN picks **2** (the smallest).
Now α at the MAX node is updated to 2.
When we begin evaluating the right MIN node, its first child returns a value ≤ 2.
Since MIN will only go lower, MAX already has a path worth 2 from the left child — the entire right subtree can be pruned.

#### Complexity Reduction

Without pruning, minimax visits **O(b^d)** nodes where `b` is the branching factor and `d` is the depth. With perfect move ordering, alpha-beta reduces this to **O(b^(d/2))** — effectively doubling the searchable depth for the same computation. For Tic-Tac-Toe:

| Metric | Plain Minimax | With Alpha-Beta |
|--------|--------------|-----------------|
| Nodes visited (from empty board) | ~550,000 | ~30,000 |
| Effective branching factor | ~4–5 | ~2–3 |

The result is identical either way — alpha-beta is a pure optimisation.

### 4. Why the AI Guarantees a Tie

The guarantee follows from two facts:

1. **Minimax is optimal**: Given a complete game tree, minimax selects the move that leads to the best achievable outcome under the assumption that the opponent also plays optimally. This is a proven property of the algorithm (von Neumann, 1928).

2. **Tic-Tac-Toe's game-theoretic value is a draw**: Exhaustive enumeration of all 5,478 reachable positions confirms that from the starting (empty) board, the minimax value is 0 (a draw). Neither player can force a win against optimal opposition.

Combining these:
- If the opponent plays optimally → the game ends in a **draw** (the game-theoretic value).
- If the opponent plays sub-optimally → the AI exploits the mistake, and the game ends in an **AI win** (the AI's minimax value for the resulting sub-tree is > 0).
- The AI never loses because it never selects a move whose minimax value leads to a forced loss.

Therefore, the AI **guarantees at least a tie in every game**.

### 5. Game State Space Summary

| Property | Value |
|----------|-------|
| Board cells | 9 |
| Upper bound of game sequences (9!) | 362,880 |
| Unique reachable board positions | 5,478 |
| Positions after symmetry reduction | 765 |
| Game-theoretic value | **Draw (0)** |
| Possible outcomes with optimal play | Always a draw |
| Lines to check for a win | 8 (3 rows + 3 columns + 2 diagonals) |

### 6. References

- **Zermelo, E.** (1913). "On an Application of Set Theory to the Theory of the Game of Chess." — First proof that finite perfect-information games are determined.
- **Von Neumann, J.** (1928). "On the Theory of Parlor Games." — Foundation of the minimax theorem for zero-sum games.
- **Knuth, D. E. & Moore, R. W.** (1975). "An Analysis of Alpha-Beta Pruning." — Formal analysis showing alpha-beta achieves O(b^(d/2)) in the best case.
- **Russell, S. & Norvig, P.** *Artificial Intelligence: A Modern Approach*, Chapter 5 — Textbook treatment of minimax and alpha-beta for game-playing agents.
