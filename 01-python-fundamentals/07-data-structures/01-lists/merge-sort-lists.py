# Q3. Input two lists of integers from the user. Merge them into one list and sort the
# result.

# Eg - list1 = [1, 2, 7] , list2 = [2, 4, 5]

# result = [1, 2, 2, 4, 5, 7]

lst1 = [1, 2, 7]
lst2 = [2, 4, 5]


mergedList = lst1+lst2

mergedList.sort()

print(mergedList)