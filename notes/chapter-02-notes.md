# Arrays

An array is a data structure that stores elements in contiguous memory locations. Each element can be accessed directly using its index.

## Characteristics

- Elements are stored sequentially in memory.
- Each element has an index (starting from 0).
- Allows fast random access.

## Time Complexity

- Access by index → O(1)
- Search (unsorted) → O(n)
- Insertion (middle or beginning) → O(n) (because elements must be shifted)
- Insertion (end, if space available) → O(1)

## Advantages

- Fast access by index.
- Simple structure.
- Good cache performance.

## Disadvantages

- Expensive insertions and deletions (except at the end).
- Fixed size (in many languages).



# Linked Lists

A linked list is a data structure where each element (node) contains a value and a reference (pointer) to the next node.

## Characteristics

- Elements are not stored contiguously in memory.
- Each node points to the next node.
- No direct index access.

## Time Complexity

- Access by index → O(n)
- Search → O(n)
- Insertion at the beginning → O(1)
- Insertion in the middle (if position known) → O(1)
- Deletion (if node reference is known) → O(1)

## Advantages

- Efficient insertions and deletions.
- Dynamic size.

## Disadvantages

- Slow access (must traverse from the head).
- Extra memory required for pointers.



# Selection Sort

Selection sort is a simple sorting algorithm that repeatedly selects the smallest element from the unsorted portion and places it at the beginning.

## How It Works

- Find the smallest element in the list.
- Swap it with the first element.
- Move the boundary of the sorted portion one step forward.
- Repeat until the list is sorted.

## Example

Unsorted list:

[5, 3, 6, 2, 10]


- Step 1: Smallest = 2 → go to index(0)
- Step 2: Smallest of remaining = 3 → go to index(1)
- Step 3: Smallest of remaining = 5 → go to index(2)
- And so on.

## Time Complexity

Always O(n²)

## Why?

Because for each element, you scan the remaining elements to find the smallest one.

## Characteristics

- Simple to understand and implement.
- Not efficient for large datasets.
- Works well for small lists.


The complete implementation can be found here:

➡️ [View selection sort implementation](../code/selection_sort.py)

# Chapter 2 exercises

➡️ [Exercises](../exercises/chapter-02-exercises.md)