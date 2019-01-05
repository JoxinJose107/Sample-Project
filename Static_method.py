
class Employee:
    def employDetails(self):
        self.name="Joxin"
    
    @staticmethod
    # Static methods are decorators that ignore the binding of the object. It is used for the methods that doesnt make use of the self keyword.
    #Decorators are function that takes another function and extends its functionality. Denoted by @ symbol at the beginning
    
    def welcome():
        print("Welcome to our organisation")


employee1=Employee()
employee1.welcome()
# print(employee1.name)