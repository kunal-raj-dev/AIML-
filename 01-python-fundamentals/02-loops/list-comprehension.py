# 0,1,4,9,16,25,
lst1 = []
for i in range(6):
    lst1.append(i*i)

print(lst1)

# 0,1,4,9,16,25,
lst2 = [i*i for i in range(6)]
print(lst2)


# sum of all even number till 10 via list comprehension
lst3 = sum([i for i in range(11) if i%2==0])
print(lst3)