# Q5. Create a dictionary where:

# . Keys = student names

# · Values = marks (integer)
# Write a menu-based program where user presses a key ('A', 'B', 'C', 'D')
# depending on the operation they want to perform on the dictionary:

# 1. A - Add a student

# 2. B - Update marks

# 3. C - Search for a student

# 4. D - Display all students and marks


def menu():
    print("""

OPERATION MENU :
A - Add a student
B - Update marks
C - Search for a student
D - Display all students and marks
""")
    choice = input("Enter choice (Q for quit) : ").upper()
    return choice


def addStudent():
    name = input("Enter student name : ")
    marks = int(input("Enter marks : "))
    marks_dict[name] = marks
    print("Added successfully.")

def updateMarks():
    if len(marks_dict) != 0:
        name = input("Enter name whose marks to change : ")
        if name in marks_dict:
            marks = int(input("Enter new marks : "))
            marks_dict[name] = marks
        else:
            print(f"{name} not in data.")
    else:
        print("Dict is Empty.")

def searchStudent():
    if len(marks_dict) != 0:
        search_query = input("Enter name to search : ")
        if search_query in marks_dict:
            print(f"{search_query} : {marks_dict[search_query]} marks")
        else:
            print("Not found.")
    else:
        print("Dict is empty")

def displayData():
    if len(marks_dict) != 0:
        print("Student and marks :")
        for stu in marks_dict:
            print(f"{stu} = {marks_dict[stu]}")
    else:
        print("No data to display.")

marks_dict = {}

while True:

    menu_choice = menu()

    if menu_choice == 'A':
        addStudent()

    elif menu_choice == 'B':
        updateMarks()

    elif menu_choice == 'C':
        searchStudent()

    elif menu_choice == 'D':
        displayData()

    elif menu_choice == 'Q':
        break

    else:
        print("Invalid choice.")