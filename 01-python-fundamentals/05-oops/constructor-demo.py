class Student:
    college_name = "IIT"

    # constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

s1 = Student("Rahul", 21, "male")
s2 = Student("Meera", 20, "female")

print(f"Student 1: {s1.name}, {s1.age} yrs, {s1.gender} ({s1.college_name})")
print(f"Student 2: {s2.name}, {s2.age} yrs, {s2.gender} ({s2.college_name})")

