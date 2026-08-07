# Number Problems Notes

## Important Concepts
- Modulo operator `%`: Extracts remainders (essential for digit checking and prime calculations).
- Integer division `//`: Discards remainders (used to strip digits off integers).
- Digit isolation loops: Repeatedly using `% 10` and `// 10` to process number components.

## Common Mistakes
- Infinite division loops (forgetting to update variables using `num //= 10` inside loops).
- Float division errors: using `/` instead of `//` when isolating digits, converting integers into floats.
- Incorrect checks for prime factors (stopping checks too early or iterating unnecessary ranges).

## Interview Notes
- **How do you reverse an integer mathematically without string conversions?** Loop: extract last digit using `remainder = num % 10`, build result using `reversed_num = (reversed_num * 10) + remainder`, and strip digit using `num = num // 10`.
- **What is the most optimized range to check for prime numbers?** Check up to the square root of the number (`int(num ** 0.5) + 1`), since factors repeat after that point.

## Practice Ideas
- Build an Armstrong number checker (sum of digits raised to power of digit count equals original number).
- Write a program to print the prime factorization of any given integer.
