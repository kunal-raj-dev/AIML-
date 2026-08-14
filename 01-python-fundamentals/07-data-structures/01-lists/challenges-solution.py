def clean_list(numbers):
    if len(numbers) < 3:
        return None
    
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    
    # Remove the smallest and largest values (outliers)
    cleaned = sorted_numbers[1:-1]
    
    # Calculate and return the median of the remaining numbers
    n = len(cleaned)
    if n % 2 == 1:
        return cleaned[n // 2]
    else:
        return (cleaned[n // 2 - 1] + cleaned[n // 2]) / 2

# Example testing:
if __name__ == "__main__":
    test1 = [10, 1, 5, 3, 9, 20]
    test2 = [5, 100, 1, 2, 8]
    print(f"clean_list({test1}) -> {clean_list(test1)}")
    print(f"clean_list({test2}) -> {clean_list(test2)}")
