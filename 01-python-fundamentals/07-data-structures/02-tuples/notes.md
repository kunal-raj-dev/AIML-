# Tuples Notes

## Important Concepts
- Tuples: Immutable ordered sequences of values.
- Tuple creation: single item tuples require trailing commas `(val,)`.
- Immutability: tuples cannot be altered after creation (secures data integrity).

## Common Mistakes
- Trying to mutate a tuple value directly, causing a `TypeError`.
- Defining single element tuples without a trailing comma, e.g. `x = (5)` which evaluates to a standard integer instead of a tuple.

## Interview Notes
- **Why use tuples when lists exist?** Tuples are immutable, making them safer for constant data definitions. They are hashable (can be dictionary keys), and offer minor memory/speed optimizations in Python.

## Practice Ideas
- Write a program that swaps two variables using tuple unpacking (`a, b = b, a`).
