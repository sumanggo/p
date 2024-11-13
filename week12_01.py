# week12_01.py

class Subject:
    def setGrade(self, grade):
        if grade != None and (grade < 0 or grade > 4.5):
            grade = None
        self.grade = grade
    
    def __init__(self, number, name, teacher=None, grade=None):
        self.number = number
        self.name = name
        self.teacher = teacher
        self.setGrade(grade)
        
    def __str__(self):
        return f"[{self.number}] {self.name}"
'''
sub = Subject("CS0001", "컴퓨터개론", grade=100.9)
print(sub.grade)

sub = Subject("CS0001", "컴퓨터개론", grade=100.9)
sub.setGrade = 100.9
print(sub.grade)

sub = Subject("CS0001", "컴퓨터개론")
print(sub.grade)
'''
class Student:
    def totalGrade(self):
        if self.subjects:
            grades = [sub.grade for sub in self.subjects if sub.grade != None]
            if grades:
                return sum(grades) / len(grades)
        else:
            print("수강과목이 없어")
            return None
    
    def __init__(self, number, name, dept, birthyear, *subjects):
        self.number =  number
        self.name = name
        self.dept = dept
        self.birthyear = birthyear
        if subjects:
            self.subjects = list(subjects)
        else:
            self.subjects = list()

    def __str__(self):
        return f"[{self.number}] {self.name}"

st = Student("1", "김현준", "컴정", 2024)
print(st)
print(st.totalGrade())

st = Student("2", "김준현", "컴정", 2024
            , Subject("001", "파이썬", "김인하")
            , Subject("002", "자바스크립트", "이인하")
             )
print(st)
print(st.totalGrade())

st = Student("3", "현준김", "컴정", 2024
            , Subject("001", "파이썬", "김인하", grade = 4.5)
            , Subject("002", "자바스크립트", "이인하")
            , Subject("003", "오픈소스", "박인하", grade = 4.0)
             )
print(st)
print(st.totalGrade())


    
