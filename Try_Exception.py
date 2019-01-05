#***************** Try Exception ***********

try:
    value=int(input("Enter the number"))
    print(value)

except:
    print("Invalid Input")



########################

try:
    value1=int(input("Enter the number"))
    print(value1)

except ValueError:
    print("Invalid Intput")

#####Zero Division Error
# Storing the exception into a variable
try:
    num=10/0
    print(num)
except ZeroDivisionError as err:
    print(err)
