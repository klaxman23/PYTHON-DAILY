#Write a program to find the character is palindrome and not?


name = input("Enter a name:")

name1 = name[::-1]

if name == name1:
    print("It is palindrome")
else:
    print("it is not a palindrome")