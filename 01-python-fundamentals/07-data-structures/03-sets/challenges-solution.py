import string

def get_words(sentence):
    # Ignore punctuation by replacing it with space to avoid joining words
    cleaned = ""
    for char in sentence:
        if char not in string.punctuation:
            cleaned += char
        else:
            cleaned += " "
    return set(cleaned.lower().split())

def main():
    sentence1 = input("Enter first sentence: ")
    sentence2 = input("Enter second sentence: ")
    
    words1 = get_words(sentence1)
    words2 = get_words(sentence2)
    
    shared = words1.intersection(words2)
    unique = words1.symmetric_difference(words2)
    
    print("\nShared words (intersection):", sorted(list(shared)))
    print("Unique words (symmetric difference):", sorted(list(unique)))

if __name__ == "__main__":
    main()
