# Q4
# . Write a function to return the  count the number of digits in a number , n.

def countDigit_via_modulo(n):
    i = 0
    while(n>0):
        i+=1
        n //= 10
        
    return i    


def countDigit_via_str(n):
    # string = str(n)
    count = 0
    for i in str(n):
        count += 1
        
    return count

def countDigit_via_len(n):
    return len(str(n))

n = int(input("enter num : "))
print(f"total digits in {n} is {countDigit_via_modulo(n)}")
print(f"total digits in {n} is {countDigit_via_str(n)}")
print(f"total digits in {n} is {countDigit_via_len(n)}")
