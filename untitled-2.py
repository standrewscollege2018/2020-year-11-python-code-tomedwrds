class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def func(self):
        print("My name is " + self.name)
        
        
p1 = Person("Tom",15)

p1.func()
        
