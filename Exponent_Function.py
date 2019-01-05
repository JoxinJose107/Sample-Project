
# ******Exponent Function***********
# Exponent function basically allow us to take a certain number and raise it to a specific power.

print("Program to find the exponent of a number")
base_number=int(input("Enter the base number: "))
pow_number=int(input("Enter the power number: "))
result=1
for i in range(pow_number):
    result=result*base_number

print("The result is: "+ str(result))


# Using function

def raise_to_power(base,pow):
    result=1
    for i in range(pow):
        result=result*base

    return result

print("The exponent is : "+str(raise_to_power(4,3)))


