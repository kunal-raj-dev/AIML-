# Q10. Ask the user for a string and print:

# . All unique characters

# . The count of unique characters

text = input("Enter a string: ")

unique_chars = set(text)

print("Unique characters:", unique_chars)
print("Count of unique characters:", len(unique_chars))