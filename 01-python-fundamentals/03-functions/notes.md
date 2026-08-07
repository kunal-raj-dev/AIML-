# Functions Notes

## Important Concepts
- `def` keyword: Defines a new reusable function.
- Arguments & Parameters: Values passed into functions.
- `return` statement: Exits a function and passes back a result to the caller.
- Default parameters: Parameters that assume fallback values if omitted.
- Lambda functions: Single-line anonymous functions (`lambda x: x * 2`).

## Common Mistakes
- Forgetting to write the `return` statement, causing functions to evaluate to `None` implicitly.
- Defining mutable default parameters (like lists `[]`) which persist changes across function calls.
- Confusing print statements (`print()`) with returning values (`return`).

## Interview Notes
- **What is the difference between *args and **kwargs?** `*args` collects positional arguments as a tuple, while `**kwargs` collects keyword arguments as a dictionary.
- **What is the scope of variables declared inside a function?** Variables defined inside a function are local to that function and cannot be accessed from the outside (local scope vs global scope).

## Practice Ideas
- Create a temperature converter module using separate functions for Celsius and Fahrenheit.
- Write a function that calculates compound interest using optional keyword arguments for rate and terms.
