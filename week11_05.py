# week11_05.py

class Test:
    def __init__(self):
        self.name = None
        self.age = None
        
    def func(self, name, age):
        self.name =  name
        print(age)

t = Test()
print(t.name)
print(t.age)

t = Test()
t.func("김인하", 20)
print(t.name)
print(t.age)

print("-" * 20)

class In:
    def func(self):
        print("In.func()")

class Out:
    def method(self):
        print("Out.method()")

#method()
#func()

#Out.method()
#In.func()

i = In()
o = Out()

Out.method(o)
In.func(i)

o.method()
i.func()

#되지만 정상적으로 동작하지 않을 가능성이 큼.
Out.method(i)
In.func(o)
