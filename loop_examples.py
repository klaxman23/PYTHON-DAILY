#Write a program for the range function.
for i in range(11):
    print(i)
    
else:
    print("Sucessfully completed.")

##############################################

#Write a program to print the all the list of items.

fruits = ["Banana","Orange","Grapes","Sapota","Apple"]

for i in fruits:
    print(i)
###########################

#Write a program to break the loop.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
############################################
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
############################

for i in range(1,6):
    if i==3: break
    print(i)
else:
    print("Finally finished!!")
    
########################################
#Write a program fo continue the loop.
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for i in adj:
    for j in fruits:
        print(i,j)
        
#######################################


for i in [1,2,3]:
    pass   
