# week11_04.py

class Student:
    def __init__(self):
        self.name = ""
        self.number = ""
        self.dept = ""
        self.birthyear = 0
students = []
for i in range(3):
    stu = Student()
    stu.name = input("이름 : ")
    stu.number = input("학번 : ")
    stu.dept = input("학과 : ")
    stu.birthyear = int(input("생년(yyyy) : "))
    students.append(stu)

for i in students:
    print(stu.name)
