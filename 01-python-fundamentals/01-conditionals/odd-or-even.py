# WAF to check if a number is odd or even.

def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter an integer: "))
result = check_odd_even(num)
print(f"{num} is {result}")
