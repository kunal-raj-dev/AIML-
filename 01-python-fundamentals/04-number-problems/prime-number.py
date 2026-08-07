num = int(input("Enter number : "))

isPrime = True

if num == 1:
    print("unique number")
elif num <= 0:
    print("Invalid input")

else:
    for i in range(2,num):
        if (num%i == 0):
            isPrime = False
            break

    if (isPrime):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is a composite number.")
    