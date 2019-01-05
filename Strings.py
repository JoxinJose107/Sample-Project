# variables are used to store data in any programming languages
#In case if there is any need to change the content or values, variables are highly useful. 
name="Joxin"
age=23
print("My name is " +name+ "and I am " +str(age)+ " years old")
# We cannot concatenate an integer with a string. so Inorder to do that we should convert int to string.


# ****Datatypes****
# 1) Strings= stores plain text
# 2) Numbers=either decimal or whole numbers
# 3) boolean

# ****WORKING WITH STRINGS****
# Inorder to create strings quotation mark should be used: print(" "), a="xyz".

name="Joxin "
print(name)

#concatenation is the process of taking a string and appending it with another string. It can be achieved by using "+" symbol.

print(name+" is a boy")
name1="Jose"
print(name+name1)

#Functions are specific block of code that performs a particular operation for us. We can use functions to modify our string, get information about our string


# lower() converts the entire string to lower case
print("String in lower case: "+name.lower())

# upper() converts the entire string to upper case.
print("String in upper case: "+name.upper())

# isupper() returns true if the entire string is in uppercase else returns false.
print(name.isupper())

# islower() returns true if the entire string is in lower case else returns false.
print(name.islower())

# We can run the combination of all these functions
# The following code snippet: upper() converts the string into uppercase then it checks whether the string is in uppercase using isupper(). The same applies with the lower() and islower().
print(name.upper().isupper())
print(name.lower().islower())

# len() is used to find the length of the character.
print(len(name))

# In python a string gets indexed starting with 0. To print a particular character from the string, mention the index value of the character in square brackets: eg[0]
print(name[0])
print(name.lower()[0])


# index() function tell us where a specific character is located inside our string.
print("The index value of J: "+str(name.index("J")))
print(name.index("in"))

# Replace function is to replace a specific string or character. replace() takes two parameters: 1) the original string 2) the new string 
print(name.replace("Jo","Re"))


