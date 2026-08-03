# Loops Notes

## Important Concepts
- `while` loops: Execute code blocks continuously as long as a condition is True.
- `for` loops: Iterate over sequences (lists, ranges, strings, tuples).
- `break`: Exits the loop entirely immediately.
- `continue`: Skips the current iteration and jumps to the next loop evaluation.
- `range(start, stop, step)`: Generates an arithmetic progression sequence of integers.

## Common Mistakes
- Creating infinite loops by forgetting to increment the loop variable inside a `while` loop.
- Off-by-one errors with `range(start, stop)` because the `stop` parameter is exclusive.
- Using `break` incorrectly, exiting loops prematurely before completing calculations.

## Interview Notes
- **What is loop-else in Python?** A `for` or `while` loop can have an `else` block. The `else` block executes when the loop finishes normally (i.e. is not terminated prematurely by a `break` statement).
- **When should you use a for loop vs. a while loop?** Use a `for` loop when you know the number of iterations beforehand (iterating over a sequence). Use a `while` loop when looping depends on a dynamic condition being met.

## Practice Ideas
- Build a password entry system that locks the user out after 3 incorrect attempts using loops.
- Create a Fibonacci sequence generator printing terms up to a user-provided limit.
