def is_palindrome(n):
    if n < 0:
        return False
    original = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev == original

s = input('Enter an integer: ').strip()
try:
    num = int(s)
except:
    print('Please enter a valid integer.')
else:
    if is_palindrome(num):
        print('The integer is a palindrome.')
    else:
        print('The integer is not a palindrome.')
