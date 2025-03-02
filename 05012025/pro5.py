class Person:
    def __init__(self,name,age,rollnumber):
        self.name = name
        self.age = age
        self.rollnumber = rollnumber
        
p1 = Person("John",25,1001)
p2 = Person("Mohan",23,1002)

print("Name","Age","Roll_number")
print(p1.name,p1.age,p1.rollnumber)
print(p2.name,p2.age,p2.rollnumber)      
        