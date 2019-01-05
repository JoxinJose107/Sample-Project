
# ************8Using If statement and comparison***********

# Using comparison we can compare two diferent values, the values can be anything, it can be string, numbers, decimals, boolean etc..Depending on the result of certain comparison we can do certain things.

# Creating a function that returns the largets number. There are three parameters to the function i.e 3 numbers

def larger_number(num1,num2,num3):
    if num1>=num2 and nu1>=num3:
        print(str(num1)+" is largest")
    elif num2>=num1 and num2>=num3:
        print(str(num2)+ " is largest")
    elif num3>=num1 and num3>=num2:
        print(str(num3)+" is largest")
    else:
        print("Congratulations!!! You are fired...")
    
larger_number(1,2,3)

# Comparison statements are:
# <= less than equal to
# >= greater than equal to
# == check whether two values are equal or not.