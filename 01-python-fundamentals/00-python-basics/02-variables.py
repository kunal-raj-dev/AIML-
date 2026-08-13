# 02. Variables in Python
# A variable is a named memory location used to store data.

# Variable assignment
student_name = "Rahul Sharma"
student_age = 20
marks_percentage = 94.5
is_enrolled = True

# Python is dynamically typed (type determined at runtime)
x = 100
print(f"x initially: {x} (type: {type(x)})")

x = "Now I am a string"
print(f"x reassigned: '{x}' (type: {type(x)})")

# Multiple assignment
a, b, c = 10, 20, 30
print(f"a={a}, b={b}, c={c}")

# Rules for naming identifiers:
# 1. Must start with letter or underscore (_)
# 2. Cannot start with a digit
# 3. Can contain letters, digits, and underscores
# 4. Case-sensitive (age vs Age vs AGE)
# 5. Cannot use Python reserved keywords
_valid_var_123 = "Valid Variable"
print(_valid_var_123)
