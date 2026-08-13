class Employee:
    start_time = "10am"
    end_time = "6pm"

    def changeTime(self, newEndTime):
        self.end_time = newEndTime

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject
    
    def changeTime_1(self, newEndTime):
        self.end_time = newEndTime

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

t1 = Teacher("Maths")
print(f"{t1.subject} - {t1.start_time} to {t1.end_time}")

t2 = t1

t1 = Teacher("Eng")
print(f"{t1.subject} - {t1.start_time} to {t1.end_time}")
print(f"{t2.subject} - {t2.start_time} to {t2.end_time}")

a1 = AdminStaff("Manager")

t1.changeTime("5pm")
print(f"{t1.subject} - {t1.start_time} to {t1.end_time}")

t1.changeTime_1("2pm")
print(f"{t1.subject} - {t1.start_time} to {t1.end_time}")
