# Q3
# . Write a function that prints the  
# n = 312
# digits
# n
# of a number, . 
# For eg:  , there are 3 digits in it 3, 1 and 2 & we need to print them.
# [ 
# Hint- The right most digit of a number N is N%10. 
# And to remove the right most digit from a number, we can do N = N / 10.]
def printDigit_via_str(number):
    for digit in str(n):
        print (digit, end=",")

def printDigit_via_modulo(number):
    while(n > 0):
        lstDigit = n%10
        print(lstDigit, end=",")
        n //= 10


n = int(input("Enter a number : "))

printDigit_via_str(n)
printDigit_via_modulo(n)