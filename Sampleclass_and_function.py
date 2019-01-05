
class Student:
    # global name,age,university 
    def __init__(self):
        self.name=input("Enter the name: ")
        self.age=int(input("Enter the age: "))
        self.university=input("Enter the name of the University: ")
        self.mark=int(input("Enter the marks: "))

    def display_data(self):
        print("The name of the Student is: "+self.name)
        print("The age of " + self.name + " is: "+str(self.age))
        print("The name of the University is :"+self.university)
        print("The mark is :"+str(self.mark))
        if self.mark <50:
            print("Congratulations!!!! You have successfully failed...!!!")
        else:
            print("Oops!!!..Unfortunately you have passed...!!")
        if self.university=="Christ University" or self.university=="CHRIST UNIVERSITY":
            print("You are Screwed!!!")
        else:
            print("Good Choice!!")


student1=Student()
# print(student1.read_data())
student1.display_data()