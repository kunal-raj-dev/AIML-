# Data Structure Console Projects Notes

## Important Concepts
- Combining complex nested data collections (dictionaries with set values).
- CLI interface menus tracking multiple data operations.

## Common Mistakes
- Improper dictionary value initialization: adding items to nested sets before the set key is instantiated (use `dict.setdefault(key, set()).add(val)` to avoid this).

## Interview Notes
- **What is the benefit of using sets as dictionary values?** It enforces uniqueness on the values mapped to each key, preventing duplicate records automatically.

## Practice Ideas
- Build a contacts directory console application supporting name updates and multiple phone numbers per contact.
