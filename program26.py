#Write a program to add the set value to list values.

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)


#Write a program set of items remove 1 item in the set.

thisset = {"Orange","grapes","mango","apple"}

thisset.remove("grapes")
print(thisset)

thisset.discard("grapess")
print(thisset)

#we can use pop() method
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(thisset) 

#we can use clear method

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

