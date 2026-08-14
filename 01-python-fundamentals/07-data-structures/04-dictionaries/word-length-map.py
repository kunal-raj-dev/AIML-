# Q6. Given a list of words:

# words = ["apple", "banana", "kiwi", "cherry", "mango"]

# Create a dictionary that maps each word to its length.
# Example:

# {"apple": 5, "banana": 6, "kiwi": 4, ... }

words = ["apple", "banana", "kiwi", "cherry", "mango"]

word_len = {}

for char in words:
    word_len[char] = len(char)

print(word_len)    
