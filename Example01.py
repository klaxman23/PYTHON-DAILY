#Write a program to find the lenth of the names, with use list comprehension.
names = ["Daniel","Mike","William","Kavya"]

#List comprehension

length = [len(name) for name in names]
print(length)
#Dictionary Comprehension

length = {name : len(name) for name in names}
print(length)
