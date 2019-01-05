

# ***************Reading from external files in python***********

# read command will allow you to read a file that is stored outside

#open() function will have two parameters: 1) Filename(if both python and  file resides on the same directory) or path of the file, if its on a different directory. 2)mode-(read,write,append,r+(read and write))

# Whenever we open the file, it is very much important to close it


employee_file=open("employee.txt","r")  #Opening file and storing it into a variable
print(employee_file.readable()) #readable() function tells whether the file is readable or not.It returns a boolean value.
print(employee_file.read()) #read() function spits out all the information from the file
#print("*****Printing individual lines*******")
#print(employee_file.readline()) # readline() prints the individual line,readline()[] will return the data at any specific index
#print(employee_file.readlines()) #readlines() prints the file as list
employee_file.close() #Closing the file

#it's because you're trying to read from a file whose read pointer is at the end. But the reason it's not obvious why this can't work is that you're using readlines.

# using for loop
# employee_file1=open("employee.txt","r")
# for employe in employee_file.readlines():
#     print(employe)