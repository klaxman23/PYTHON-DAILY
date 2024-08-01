#write a program for the calculation.

num = int(input("Enter a number: "))
num1 = int(input("Enter a number: "))

num2 = input("Enter a operator: ")

if num2 == "+":
    print("Result: ",num+num1)
elif num2 == "-":
    print("Result: ",num-num1)
elif num2 == "*":
    print("Result: ",num*num1)
elif num2 == "/":
    print("Result: ",num/num1)
else:
    print("invalid operator!")
 