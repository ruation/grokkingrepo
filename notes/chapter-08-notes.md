# Greedy Algorithms

A **greedy algorithm** is a problem-solving strategy that builds a solution step by step, always choosing the **locally optimal choice** at each step.

The idea is that making the best immediate choice will lead to an **optimal global solution**.

Greedy algorithms are usually simpler and faster than other approaches because they do not reconsider previous choices.

---

## Key Idea

At each step, choose the option that seems best **right now**, without worrying about future consequences.

Unlike dynamic programming, greedy algorithms **do not explore all possible solutions**.

---

## Example: Set Covering Problem

Suppose you want to cover a set of states using the **smallest number of radio stations**.

Each station covers certain states.

The greedy strategy:

1. Choose the station that covers the **largest number of uncovered states**.
2. Mark those states as covered.
3. Repeat until all states are covered.

This approach finds a **good approximation** of the optimal solution.

---

## Characteristics of Greedy Algorithms

- Make decisions **step by step**
- Always choose the **best immediate option**
- Do **not backtrack**
- Often produce **efficient approximations**

---

## Time Complexity

The complexity depends on the problem, but greedy algorithms are often **more efficient** than exhaustive approaches.

Many greedy solutions run in:

- O(log n)
- O(n)

---

## Advantages

- Simple to implement
- Fast execution
- Works well for many optimization problems

---

## Limitations

Greedy algorithms **do not always produce the optimal solution**.

They only work correctly for problems that satisfy the **greedy-choice property**.

If this property does not hold, a greedy approach may give a **suboptimal result**.

---

## Common Problems Solved with Greedy Algorithms

- Activity selection
- Huffman coding
- Minimum spanning trees (Prim's and Kruskal's algorithms)
- Set covering approximation

---

## Summary

Greedy algorithms:

- Choose the **best immediate option** at each step
- Build a solution **incrementally**
- Are usually **fast and simple**
- Work well for certain optimization problems
