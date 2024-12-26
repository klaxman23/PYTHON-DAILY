num = int(input("Enter a value: "))
num1 = int(input("Enter a value: "))
opr = input("Enter a oper: ")

if opr =="+":
    print(num+num1)
elif opr =="-":
    print(num - num1)
elif opr =="*":
    print(num * num1)
elif opr =="/":
    print(num / num1)
else:
    print("Invalid operator")
    