#Write a program to facotial.

n  = int(input("Enter a value: "))
mull = 1
for i in range(1,n+1):
    mull *= i
print("The Result:",mull)