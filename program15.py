#write a program to use class.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
p1 = Person("john",23)
p2 = Person("Mohan",26)
p3 = Person("Sankar",21)

print(p2.name,p2.age)
print(p1.name,p1.age)
print(p3.name,p3.age)
