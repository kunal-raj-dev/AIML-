
# Q7.Design a program to continuously input a number  from user & print if it is 
# positive or negative until the user enters “Quit”


def numberType(number):
    if number < 0:
        print(f"{n} is negative")

    elif number > 0:
        print(f"{n} is positive")

    else:
        print("Number is Zero")



while (True):
    n = input("Enter integer ('quit' to end) : ")

    if n == "quit":
        break
    try:
        numberType(int(n))
    except ValueError:
        print("Enter 'quit' or valid integer")
