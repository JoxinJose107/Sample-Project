
#***** Functions ****
# Functions are basically collection of codes that performs a specific task.
# Inorder to use function, it should start with a keyword 'def'.
# Any code inside the function  need to be intended.


# All the code coming inside fun_name(): is written inside function.
def say_hi(name,age): 
    print("Hello "+name+" You are "+age+" years old")


# We should call the function to make it work. Code inside the function cannot be executed by default.
say_hi("Joxin","23")

# Parameter is a piece of information that we give to function.


# Addition

def addition():
    num1=input("Enter the first number")
    num2=input("Enter the second number")
    sum=float(num1)+float(num2)
    print("The sum is "+ format(sum))

addition()
