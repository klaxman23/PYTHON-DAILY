#Write a program to small and addtion with lambda function details.

x = lambda a : a + 10
print("Result:", x(5))

x1 = lambda a : a - 10
print("Result:", x1(5))

x2 = lambda a : a * 10
print("Result:", x2(5))

x3 = lambda a : a / 10
print("Result:", x3(5))

"---------------------------------------------------------------------------------------------------------"

aa = lambda a,b : a+b

print("Total result",aa(5,66))

ab = lambda a,b : a-b

print("Total result",ab(5,66))

ac = lambda a,b : a*b

print("Total result",ac(5,66))

ad = lambda a,b : a/b

print("Total result",ad(5,66))

#################################################################################

vva = lambda a,b,c: a+b+c

print("Result:-",vva(5,5,5))

#############################################

def myfunction(n):
    return lambda a:a*n
mydop = myfunction(21)
print(mydop(2))

#############################################