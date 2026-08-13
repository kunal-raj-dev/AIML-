# 13. WAP to input 2 numbers & print their average.

def calculate_average(a, b):
    return (a + b) / 2

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number: "))

avg = calculate_average(num1, num2)

print(f"Number 1 : {num1}")
print(f"Number 2 : {num2}")
print(f"Average  : {avg}")
