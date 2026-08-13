# 05. Python Style Guide (PEP 8 Best Practices)
# Clean, readable code standards recommended by Python:

# 1. Naming Conventions:
# - Variables & functions: snake_case
total_student_count = 50

def calculate_simple_interest(principal, rate, time):
    """Calculates simple interest following PEP 8 naming & docstring."""
    return (principal * rate * time) / 100

# - Constants: UPPER_CASE_WITH_UNDERSCORES
PI = 3.14159
MAX_RETRY_LIMIT = 5

# - Classes: PascalCase (CamelCase)
class UserAccount:
    pass

# 2. Spacing and Indentation:
# - Use 4 spaces per indentation level (never mix tabs and spaces)
# - Leave spaces around binary operators (=, +, -, *, /, ==)
# - Leave 2 blank lines between top-level functions and classes

interest = calculate_simple_interest(10000, 7.5, 2)
print(f"Calculated Interest: ₹{interest}")
