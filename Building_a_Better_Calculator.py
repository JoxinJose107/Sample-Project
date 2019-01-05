
# ************Building a Better Calculator*************

num1=float(input("Enter the first number: "))
op=input("Enter the operator: ")
num2=float(input("Enter the second number: "))

if op=="+":
    print("The sum is: "+ str(num1+num2))
elif op=="-":
    print("The difference is: "+str(num1-num2))
elif op=="/":
    print("Division is: "+str(num1/num2))
elif op=="*":
    print("The product is: "+str(num1*num2))
else:
    print("Invalid Operator")

