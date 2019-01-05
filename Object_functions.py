#********Object Functions**********

# Class function is a function which can be used inside a class that can either modify the objects of that class or give us a specific information about the object.

class Student:
    def __init__(self,name,major,gpa):
        self.name=name
        self.major=major
        self.gpa=gpa

    def pass_or_fail(self):
        if self.gpa>2.5:
            return True
        else:
            return False


    
student1=Student("Joxin","Computer Science",3.5)
print(student1.pass_or_fail())