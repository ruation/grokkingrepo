# Recursion

Recursion is a programming technique where a function calls itself in order to solve a smaller version of the same problem.

Instead of solving the entire problem at once, recursion breaks it into simpler subproblems until it reaches a base case.

## Key Components

Every recursive function must have:

- Base Case – The condition that stops the recursion.
- Recursive Case – The part where the function calls itself with a smaller input.
- Without a base case, the recursion will continue forever (infinite recursion).

## Example: Factorial

- Mathematically:

n! = n × (n - 1)!

- Base case:

1! = 1

- This means:

fact(3)

3 × fact(2)

2 × factorial(1)

➡️ [View factorial with recursion implementation](../code/factorialrecursive.py)

## Time Complexity

Depends on the problem.
For factorial, the time complexity is:

O(n)

Because the function is called once for each number down to 1.

## Advantages

- Elegant and readable for certain problems
- Useful for divide-and-conquer algorithms
- Natural for tree and graph traversal

## Disadvantages

- Can use more memory
- Risk of stack overflow
- Sometimes slower than iterative solutions



# The Call Stack

- When a function is called, it is added to a structure called the call stack.

- A stack follows the rule:

LIFO (Last In, First Out)

- This means:

The last function called is the first one to finish.

# Chapter 3 exercises

➡️ [Exercises](../exercises/chapter-03-exercises.md)