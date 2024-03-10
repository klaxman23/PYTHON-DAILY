#Write a program to count the repeted string
str1 = "aaabbbbnnnccccooooooooooooooooooaa"
count = 0
output = ""
char = str1[0]
for ch in str1:
    if ch ==char:
        count = count+1
    else:
        output += str(count)+char
        char = ch
        count = 1
output += str(count)+char
print('str1 = ', output)
