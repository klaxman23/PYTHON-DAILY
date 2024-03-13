#Create a class and write a program.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print("Hello my name is : ", self.name)
        print("i am ",self.age,"old")
        
p1 = Person("John",26)

p1.myfunc()
