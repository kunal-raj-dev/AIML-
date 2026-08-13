# 03. Data Types in Python
# Python has several built-in core data types:

# 1. Integer (int)
count = 42
print(f"count: {count} | Type: {type(count).__name__}")

# 2. Floating point (float)
temperature = 36.6
print(f"temperature: {temperature} | Type: {type(temperature).__name__}")

# 3. String (str)
greeting = "Hello Python"
print(f"greeting: '{greeting}' | Type: {type(greeting).__name__}")

# 4. Boolean (bool)
is_active = True
print(f"is_active: {is_active} | Type: {type(is_active).__name__}")

# 5. NoneType (None represents absence of value)
result = None
print(f"result: {result} | Type: {type(result).__name__}")

# Checking types using isinstance()
print("Is count an integer?", isinstance(count, int))
print("Is temperature a float?", isinstance(temperature, float))
