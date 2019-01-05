#******** Return Statement******

# return statements are used to return any information from the function

def cube(num):
    cuberoot=num*num*num
    return cuberoot


result=cube(3)
print("The cube root is "+str(result))
     
# return statement allows us to give a value back to the caller.

# code coming below the return statement wont be executed in a function
# We can return string, boolean, array...anything we want.
