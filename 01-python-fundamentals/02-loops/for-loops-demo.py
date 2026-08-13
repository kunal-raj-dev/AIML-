# Demonstration of for loops in Python
# Used to iterate over sequences (strings, lists, tuples, range).

# 1. Iterating over a string
print("--- Iterating over a String ---")
word = "PYTHON"
for char in word:
    print(char, end=" ")
print()

# 2. Iterating over a list
print("\n--- Iterating over a List ---")
fruits = ["Apple", "Banana", "Cherry", "Mango"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# 3. Using for loop with else block
# The else block executes when the loop finishes normally (no break)
print("\n--- For-Else Search Demonstration ---")
target = "Cherry"
for fruit in fruits:
    if fruit == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found in the list.")
