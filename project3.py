# Write  a program to find the palindrome or not.

name = input("Enter a name: ")

rev = ""

for i in name:
    rev = i+rev

print(rev)

if name ==rev:
    print("it is a palindrome")
else:
    print("It is not a palindrome")