# Demonstration of Match-Case (Structural Pattern Matching in Python 3.10+)

day_number = int(input("Enter day of the week (1-7): "))

match day_number:
    case 1:
        day_name = "Monday"
    case 2:
        day_name = "Tuesday"
    case 3:
        day_name = "Wednesday"
    case 4:
        day_name = "Thursday"
    case 5:
        day_name = "Friday"
    case 6:
        day_name = "Saturday (Weekend!)"
    case 7:
        day_name = "Sunday (Weekend!)"
    case _:
        day_name = "Invalid day number! Please enter between 1 and 7."

print(f"Result: {day_name}")
