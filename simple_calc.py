#simple projects to create calculator
print("welcome to Anil's calc")
#asking user enter two number
a=int(input("please enter your first number"))
b=int(input("please enter your second number"))
# asking user what type of operation you want
c=input("please enter operator +, -, *, /")

#calc function
if c=='+':
    d=a+b
    print(d)
elif c=='-':
    d=a-b
    print(d)
elif c=='/':
    d=a/b
    print(d)
else:
    d=a*b
    print(d)
