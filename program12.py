#Write a program to remove the duplicate values?

arr = [1,1,2,2,3,3,4,4]
num = []
for i in arr:
    if i not in num:
        num.append(i)
print(num)

arr = [1,1,2,2,3,3,4,4]

num = set(arr)
print(num)


def merge_array(arrayA,arrayB):
    return(sorted(set(arrayA+  arrayB)))

a = [1,2,3,3,4,5,6]
b = [4,4,5,6,7,8,9]
c = merge_array(a,b)
print(c)
#Write a program to remove the duplicate values.
a = [1,2,3,3,4,5,6]
b = [4,4,5,6,7,8,9]
d = []
c = []
for i in a:
    for j in b:
      if i not in c:
          if j not in d:
           c.append(i)
           d.append(j)
print(c,d)