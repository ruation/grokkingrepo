# Binary Search O(log n)

Binary search is an efficient algorithm used to find an element in a sorted list.
Instead of checking every element one by one, it repeatedly divides the search interval in half.

## How It Works

- Look at the middle element of the list.
- If the target value is equal to the middle element, the search is complete.
- If the target value is smaller, search the left half.
- If the target value is greater, search the right half.
- Repeat the process until the element is found or the list is empty.
- Each step eliminates half of the remaining elements.

## Requirements

- The data must be sorted
- The structure must allow random access (like arrays)

# Big O Notation

Big O notation describes how the runtime of an algorithm grows as the input size increases.

It focuses on:

- The worst-case scenario
- The growth rate, not exact time

Big O does not measure seconds.
It measures how performance scales with input size.

# Chapter 1 exercises

➡️ [Exercises](../exercises/chapter-01-exercises.md)