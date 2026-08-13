# 11. Type Conversion and Type Casting in Python

# 1. Implicit Type Conversion (Automatic by Python)
int_num = 10
float_num = 4.5
sum_result = int_num + float_num  # automatically converts to float
print(f"{int_num} + {float_num} = {sum_result} (type: {type(sum_result).__name__})")

# 2. Explicit Type Casting (Manual conversion using functions)
str_val = "125"
converted_int = int(str_val)
print(f"String '{str_val}' -> int {converted_int} (type: {type(converted_int).__name__})")

float_val = float("98.6")
print(f"String '98.6' -> float {float_val}")

int_to_str = str(4500)
print(f"Int 4500 -> string '{int_to_str}'")

# Boolean casting (Falsy values: 0, "", [], {}, None, False; Truthy values: everything else)
print(f"bool(0): {bool(0)}, bool(''): {bool('')}, bool(None): {bool(None)}")
print(f"bool(42): {bool(42)}, bool('Python'): {bool('Python')}")
