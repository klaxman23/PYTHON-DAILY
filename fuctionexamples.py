#Write a python program simple def the function and print the instruction.
def my_program():
    print("I love python program!!")

my_program()
##########################################################
#Write a to print the welcome statement!!!

def welcome_statement(fname):
    print(fname + " "+ "Hello welcome!!!")
    
welcome_statement("Laxman")

##############################################
#Write a program print the fname and lname ?

def name_details(fname,lname):
    print("Welcome! ",fname + " "+ lname)
    
name_details("kadambala","Laxman")
name_details("kadambala","Suma")
name_details("kadambala","Nihal")

#Write a program python

def my_function(*kids):
    print("Hello" + " " + kids[0])
    print("Hello" + " " + kids[1])
    print("Hello" + " " + kids[2])
    print("Hello" + " " + kids[3])
    
my_function("Laxman","Suma","Kavya","Nihal")
#Write a program python
def mmy_function(food):
    for i in food:
        print(i)

fruits = ("Apple","Orange","Grapes","Banana","Lemon")

mmy_function(fruits)

#Write a program for the table with use function

def my_table(x):
    return 5 * x

print(my_table(5))



     

    