n = int(input("Find sum till (n) number : "))

sum = 0
for i in range(1,n+1):
    sum += i

print(f"Sum of first {n} numbers is {sum}")


# sum1 = (n*(n+1)) / 2
# print(f"Sum of first {n} numbers is {sum1}")
