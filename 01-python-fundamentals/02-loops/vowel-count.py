# WAP to count the number of vowels in a given string using a loop.

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

text = input("Enter a string: ")
total_vowels = count_vowels(text)
print(f"Total vowels in '{text}': {total_vowels}")
