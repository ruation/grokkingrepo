# 📌 Divide & Conquer

## Divide & Conquer is a problem-solving strategy where you:

- Divide the problem into smaller subproblems
- Conquer the subproblems by solving them (usually recursively)
- Combine the solutions to solve the original problem

## Key Idea

- Break a big problem into smaller pieces until they become simple enough to solve directly.
- Structure Pattern

## Most Divide & Conquer algorithms follow this pattern:

if problem is simple:
    solve directly (base case)
else:
    divide problem
    solve subproblems recursively
    combine results

## Examples

- Binary Search
- Merge Sort
- Quicksort



# ⚡ Quicksort

Quicksort is a sorting algorithm based on Divide & Conquer.

## How It Works

- Choose a pivot element.
- Partition the array:
- Elements smaller than pivot → left side
- Elements greater than pivot → right side
- Recursively apply Quicksort to left and right subarrays.
- Combine results (automatically sorted after recursion).

## Example

Array:

[10, 5, 2, 3]

Choose pivot = 10

Split:

[5, 2, 3]  10  []

Then sort [5, 2, 3] recursively.

## ⏱ Time Complexity

- Best case: O(n log n)
- Average case: O(n log n)
- Worst case: O(n²) (when pivot is always smallest or largest)

## 📦 Space Complexity

- O(log n) (due to recursion stack in average case)

## Why Quicksort is Fast in Practice

- Very efficient average performance
- Good cache performance
- Often faster than other O(n log n) algorithms in real-world usage

➡️ [View quicksort implementation](../code/quicksort.py)



# Big O notations

the constant can matter sometimes. That's why quicksort is faster than merge sort.