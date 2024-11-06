# week11_03.py

class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

p = Point()
print(p.x, p.y)

class Rectangle:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.width = 0.0
        self.height = 0.0

class Subject:
    def __init__(self):
        self.number = ""
        self.name = ""
        self.teacher = ""
        self.grade = 0.0

class Studnt:
    def __init__(self):
        self.name = ""
        self.number = ""
        self.dept = ""
        self.birthyear = 0

class Rectangle2:
    def __init__(self):
        self.width = 0.0
        self.height = 0.0
        self.spoint = Point()

class Rectangle3:
    def __init__(self):
        self.spoint = Point()
        self.epoint = Point()

r = Rectangle3()
r.spoint.x = 1
r.spoint.y = 1

r.epoint.x = 10
r.epoint.x = 21
