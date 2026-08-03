# Conditionals Notes

## Important Concepts
- `if` statements: Execute code blocks when conditions evaluate to True.
- `elif` (else-if) statements: Allow checking multiple conditional expressions sequentially.
- `else` statements: Define a fallback block executed when no other conditions match.
- Comparison operators: `==` (equal), `!=` (not equal), `<`, `>`, `<=`, `>=`.
- Logical operators: `and` (both true), `or` (at least one true), `not` (reverse state).

## Common Mistakes
- Forgetting colons (`:`) after conditional statement headings.
- Indentation mistakes (mixing spaces and tabs, or inconsistent indentation spaces).
- Using variable assignments `=` instead of equality comparisons `==`.
- Writing overlapping check logic (e.g. `30000 <= salary >= 70000` which means `salary <= 30000` AND `salary >= 70000` in standard operator precedence evaluation).

## Interview Notes
- **What is the difference between multiple `if` blocks vs. `if-elif-else` chains?** Multiple `if` statements evaluate every single condition independently. In contrast, `if-elif-else` forms a single logical structure where execution exits as soon as one condition evaluates to True.
- **How does short-circuit evaluation work in Python?** In `A and B`, if A is False, B is not evaluated. In `A or B`, if A is True, B is not evaluated. This optimizes execution speed.

## Practice Ideas
- Build a movie ticket pricing calculator based on age (Child, Adult, Senior) and showtime discounts.
- Write a basic coordinate quadrant detector determining which quadrant a point (x, y) resides in.
