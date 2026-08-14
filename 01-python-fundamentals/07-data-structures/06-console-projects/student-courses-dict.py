# Given a list of tuples with info(name, subject):

# · list all unique course
# . list students enrolled in English
# · create dictionary (student,set of course)

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English") 
]


unique_course = set()
for name , course in info:
    unique_course.add(course)

print(f"\nUnique courses : {unique_course}")


course_eng_stu = set()
for name , course in info:
    if course == "English":
        course_eng_stu.add(name)

print(f"\nStudents enrolled in English : {course_eng_stu}")


stu_enrolled_course = {}

for name, course in info:
    if name not in stu_enrolled_course:
        stu_enrolled_course[name] = set() # alice : set{}
    stu_enrolled_course[name].add(course)


print("\nStudent and course details.")
for i in stu_enrolled_course:
    print(f"{i} : {stu_enrolled_course[i]}")
