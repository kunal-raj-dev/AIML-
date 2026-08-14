def cipher(text):
    vowels = "aeiouAEIOU"
    result = []
    for char in text:
        if char.isalpha():
            if char in vowels:
                result.append(char.upper())
            else:
                result.append(char.lower())
        else:
            result.append(char)
    return "".join(result)

def main():
    sentence = input("Enter a sentence: ")
    encrypted = cipher(sentence)
    print("Ciphered text:", encrypted)

if __name__ == "__main__":
    main()
