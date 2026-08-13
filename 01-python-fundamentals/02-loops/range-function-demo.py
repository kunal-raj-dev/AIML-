# Demonstration of the range() function in Python
# range(stop) -> 0 to stop-1
# range(start, stop) -> start to stop-1
# range(start, stop, step) -> start to stop-1 stepping by step

print("--- 1. range(stop) ---")
for i in range(5):
    print(i, end=" ")
print()

print("\n--- 2. range(start, stop) ---")
for i in range(2, 7):
    print(i, end=" ")
print()

print("\n--- 3. range(start, stop, step) ---")
for i in range(1, 10, 2):
    print(i, end=" ")
print()

print("\n--- 4. Reverse range with negative step ---")
for i in range(10, 0, -2):
    print(i, end=" ")
print()
