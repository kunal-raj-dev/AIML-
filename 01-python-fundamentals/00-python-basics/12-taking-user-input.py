# 12. Taking User Input in Python
# The input() function always returns user input as a string (str).

# 1. Reading string input
user_name = input("Enter your name: ")

# 2. Reading integer input (requires int() casting)
user_age = int(input("Enter your age: "))

# 3. Reading float input (requires float() casting)
user_height = float(input("Enter your height in meters (e.g. 1.75): "))

print("\n--- User Profile ---")
print(f"Name   : {user_name}")
print(f"Age    : {user_age} years old")
print(f"Height : {user_height} m")
