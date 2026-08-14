# Q9. Given a list, print all elements that appear more than once in the list.
# [Hint - use sets]

lst = [1,2,2,2,4,8,3,3]

num_register = set()
num_duplicate = set()

for i in lst:
    if i in num_register:
        num_duplicate.add(i)
    else:
        num_register.add(i) 

print("elements more than once" , num_duplicate)           
