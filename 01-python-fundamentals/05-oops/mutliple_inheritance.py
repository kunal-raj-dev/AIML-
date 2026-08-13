class Teacher:
    def __init__(self , salary):
        self.salary = salary

class Student:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher , Student):
    def __init__(self , salary , gpa , name):
        super().__init__(salary)
        Student.__init__(self , gpa)
        self.name = name

TA1 = TA(10_000 , 7.9 , "Rahul")
print(f"{TA1.name} has a salary {TA1.salary} and GPA = {TA1.gpa}")          
