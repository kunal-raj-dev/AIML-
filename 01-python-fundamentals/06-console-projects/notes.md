# Console Projects Notes

## Important Concepts
- Command Line Interface (CLI) design.
- Robust user input loops and parsing.
- Random module configurations (`random.randint`).
- Control flow combination (combining loops, functions, and conditionals).

## Common Mistakes
- Missing error handling: program crashes when user input cannot be parsed (e.g. typing text when integers are expected).
- Infinite recursion: using recursive function calls to restart game menus instead of standard `while` loops, causing StackOverflow risks.

## Interview Notes
- **How do you handle invalid inputs safely in console applications?** Use a `try-except ValueError` block nested inside a `while True` loop, forcing input prompts repeatedly until valid data is parsed.

## Practice Ideas
- Build a Rock-Paper-Scissors game playing against an AI player featuring round score updates.
- Build a text-based inventory system storing item counts and prices.
