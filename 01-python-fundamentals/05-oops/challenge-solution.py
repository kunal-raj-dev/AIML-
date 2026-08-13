class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if len(self.grades) == 0:
            return 0

        total = 0
        for grade in self.grades:
            total += grade

        return total / len(self.grades)


student1 = Student("Aman", 101)
student2 = Student("Riya", 102)

student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)

student2.add_grade(92)
student2.add_grade(88)
student2.add_grade(95)

print(f"{student1.name} average: {student1.get_average():.2f}")
print(f"{student2.name} average: {student2.get_average():.2f}")