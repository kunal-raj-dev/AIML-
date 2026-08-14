# Strings Notes

## Important Concepts
- Strings: Immutable sequences of Unicode characters.
- Slicing syntax: `text[start:stop:step]` (reversing strings using `text[::-1]`).
- String methods: `.strip()`, `.replace()`, `.split()`, `.join()`, `.count()`.

## Common Mistakes
- Trying to mutate characters in a string directly, causing `TypeError` (strings are immutable).
- Using inefficient string additions (`+`) in loops (use `.join()` instead to save memory).

## Interview Notes
- **Why are strings immutable in Python?** Immutability allows strings to be hashable (usable as dict keys), ensures memory sharing optimizations (string interning), and guarantees security in multi-threaded environments.

## Practice Ideas
- Build a sentence word reverser (e.g. 'Hello World' to 'World Hello') using `.split()` and `.join()`.
