# Q1. Ask the user for a string and check whether it is a palindrome or not.
# A palindrome is a string which is same when we read it forward & backward. Eg -
# "madam", "racecar" etc.

def isPalindrome(text):
    return text == text[::-1]

text = input("Enter a string : ")


if isPalindrome(text):
    print("Is palindrome")

else:
    print("Not a palindrome")