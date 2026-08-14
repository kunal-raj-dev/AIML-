# Q4. Given a tuple of integers, create:
# . A tuple of all even numbers

# . A tuple of all odd numbers

num = (1, 2, 3, 4, 5, 6, 7, 8)

even_tup = ()
odd_tup = ()

for i in num:
    if i % 2 == 0:
        even_tup = even_tup + (i,)
    else:
        odd_tup = odd_tup + (i,)    

print(f"even numbers : {even_tup}")        
print(f"odd numbers : {odd_tup}") 