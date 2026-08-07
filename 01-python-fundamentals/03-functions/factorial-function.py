def calcFactorial(n):
    fac = 1
    for i in range(1,n+1):
        fac *= i
    return fac

n = int(input("Enter n : "))
print(f"Factorial of {n} is { calcFactorial(n) }")
