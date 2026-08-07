# Q5. Write a function to return the sum of digits of a number,n.
def digitSum_via_str(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)

    return sum

def digitSum_via_modulo(number):
    sum = 0
    while (number > 0):
        lstDigit = number % 10
        sum += lstDigit
        number //= 10

    return sum

n = int(input("enter number : "))
print(f"Sum of digits of {n} = {digitSum_via_str(n)}")
print(f"Sum of digits of {n} = {digitSum_via_modulo(n)}")