# Demonstration of Nested Conditional Statements in Python

age = int(input("Enter your age: "))

if age >= 18:
    has_license = input("Do you have a driving license? (yes/no): ").lower()
    
    if has_license == "yes":
        print("You are legally eligible to drive a vehicle.")
    else:
        print("You are of legal age, but you must obtain a license before driving.")
else:
    years_left = 18 - age
    print(f"You are underage. You can apply for a license in {years_left} year(s).")
