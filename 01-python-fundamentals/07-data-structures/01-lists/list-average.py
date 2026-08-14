# Q2. Given a list of integers compute the average of all numbers in the list.

# num = list(int(input("enter numbers : ")))

num = [1,2,3,4,5,6,7]

total = sum(num)

average = total / len(num)

print(f"Average = {average}")
