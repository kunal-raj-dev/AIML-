# Dictionaries Notes

## Important Concepts
- Dictionaries: Key-value mapped pairings.
- Keys must be hashable types (strings, numbers, tuples).
- Retrieval methods: `.get(key, default)`, `.keys()`, `.values()`, `.items()`.

## Common Mistakes
- Accessing missing keys directly using `dict[key]` (causes a `KeyError`; use `.get(key)` to return defaults safely).
- Using mutable items (like lists `[]`) as dictionary keys.

## Interview Notes
- **How do you iterate through a dictionary's keys and values simultaneously?** Use the `.items()` method with loop unpacking: `for key, value in my_dict.items():`.

## Practice Ideas
- Write a letter frequency counter that builds a dictionary counting occurrences of characters in a string.
