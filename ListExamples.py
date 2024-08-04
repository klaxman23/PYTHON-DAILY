#Write a program to print the list of the all items.
my_list = ["Apple","Orange","Grapes","Lemon"]
print(my_list) # Here printing the all list of items.

print(my_list[0]) # here access the inside the list first element.

my_list[0] = "Green Apple" # here modifying the first element inside the list.

print(my_list) # After the modify the list print the all elements.

print("Total length of the elements will show:",len(my_list)) #it will show the present count of the lisrt.

#Write a program to print the list of the items one by one.
my_list = ["Apple","Orange","Grapes","Lemon"]
for i in my_list:
    print(i)
    
my_list.append("Green apple")
print(my_list)
my_list.pop(1)
print(my_list)
my_list.remove("Lemon")
print(my_list)

my_list.copy()
print(my_list)

my_list = ["Apple","Orange","Grapes","Lemon","Orange"]
mm=my_list.count("Orange")
print(mm)

#Write a program to reverse the element.
my_list1 = [1,2,3,4,5,6,7]

my_list1.reverse()
print(my_list1)

#Write a program to sort the element.
my_list2 = [7,2,8,99,11,55]

my_list2.sort()
print(my_list2)


