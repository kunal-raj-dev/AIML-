# Demonstration of while loops in Python
# A while loop executes a block of code as long as the condition evaluates to True.

# 1. Counting from 1 to 5
print("--- Counter using while loop ---")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# 2. Reverse counting (Countdown)
print("\n--- Countdown ---")
timer = 5
while timer > 0:
    print(f"Time remaining: {timer}s")
    timer -= 1
print("Time's up!")

# 3. Sum of numbers entered by user until 0 is entered
print("\n--- Accumulator Loop ---")
total = 0
while True:
    val = int(input("Enter number to add (0 to stop): "))
    if val == 0:
        break
    total += val
print(f"Total Sum: {total}")
