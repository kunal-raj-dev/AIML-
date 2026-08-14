# Sets Notes

## Important Concepts
- Sets: Unordered collections of unique, hashable items.
- Set operations: `.union()`, `.intersection()`, `.difference()`, `.symmetric_difference()`.
- Removing duplicate elements from sequences.

## Common Mistakes
- Creating empty sets using `x = {}` (which actually initializes an empty dictionary; use `x = set()` instead).
- Assuming sets maintain order (sets are unordered; items are hashed in arbitrary locations).

## Interview Notes
- **What is the time complexity of lookup in a List vs. a Set?** Checking membership (`item in sequence`) takes $O(n)$ linear time in a list, but $O(1)$ constant time on average in a set because sets use hash tables.

## Practice Ideas
- Find common elements between three distinct sequences using set intersections.
