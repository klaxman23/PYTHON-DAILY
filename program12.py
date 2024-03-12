#Write a program to remove the duplicate values?

arr = [1,1,2,2,3,3,4,4]

num = []
for i in arr:
    if i not in num:
        num.append(i)

print(num)