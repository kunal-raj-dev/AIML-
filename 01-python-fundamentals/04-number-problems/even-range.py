# Q2.
# Write a function that takes two integers a and b and prints all even 
# numbers between them (inclusive).
def allEven(a,b):

    lstEven = []
    for i in range(a,b+1):
        if(i % 2 == 0):
            lstEven.append(i)
        else:
            pass
        
    return lstEven    
        
        
fstNo = int(input("enter fisrt number : "))
secNo = int(input("enter second number : "))       

if fstNo < secNo:
    lst = allEven(fstNo,secNo)
    print(lst)
else:
    lst = allEven(secNo,fstNo)
    print(lst)
