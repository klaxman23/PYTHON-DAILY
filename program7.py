#Write a program to print sum of the n digits.

n = int(input("Enter a value: "))

sum = 0

for i in range(1,n+1):
    sum += i
    
print("The Result:",sum)