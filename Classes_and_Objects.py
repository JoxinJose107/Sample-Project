#******Classes and Objects*************8
#Classes and objects helps you to make your program more organised and more powerful.
# Classes and objects in python helps us to create our own datatypes.
# With class we can essentially define our own datatype.


class Student:
    def __init__(self,name,major,gpa):  #Contains the attribute of the class. Self is refering to the actual object
        self.name=name  #self.name is attribute of student and name is the value that is passed in.
        self.major=major
        self.gpa=gpa
    
student1=Student("Joxin","Computer Science",3.5)
print(student1.name)