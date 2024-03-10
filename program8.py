#Write a program to facotial.

n  = int(input("Enter a value: "))
mul = 1
for i in range(1,n+1):
    mul *= i
print("The Result:",mul)