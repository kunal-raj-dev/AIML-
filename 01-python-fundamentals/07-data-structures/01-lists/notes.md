# Lists Notes

## Important Concepts
- Lists: Mutable ordered sequences of values.
- List slicing: extracting sub-lists (`lst[start:stop:step]`).
- List methods: `.append()`, `.extend()`, `.sort()`, `.reverse()`, `.pop()`, `.insert()`.
- Loops with lists: iterating indices vs iterating items.

## Common Mistakes
- Modifying lists during iteration, causing index skips and unexpected behavior (use copy/slice `lst[:]` or list comprehensions instead).
- Confusing `.sort()` (sorts in-place, returns `None`) with `sorted()` (returns a new sorted list).

## Interview Notes
- **What is the time complexity of adding an item to the end of a list vs. inserting at index 0?** Appending (`.append()`) takes amortized $O(1)$ constant time. Inserting at index 0 (`.insert(0, val)`) takes $O(n)$ linear time because all other elements must be shifted in memory.

## Practice Ideas
- Write a function to remove duplicates from a list while maintaining original ordering.
- Perform matrix transposition using list comprehensions.
