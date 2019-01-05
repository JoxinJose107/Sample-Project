

#********* Car Rental System************
class Car:

    def __init__(self,listOfCars):
        self.availableCars=listOfCars
        self.OrignalLists=listOfCars

    def displayAvailableCars(self):
        for car in self.availableCars:
            print(car)

    def lendCar(self):
        self.entry=input("Enter the name of the car you would like to rent: ")
        self.days=int(input("Enter the number of days: "))
        if self.entry in self.availableCars:
            if self.entry == "HatchBack":
                print("Cost per day is $30")
                self.total=self.days*30
                print("Total Cost: "+str(self.total)
            elif self.entry == "Sedan":
                print("Cost per day is $50")
                self.total=self.days*50
                print("Total Cost: "+str(self.total))
            elif self.entry == "SUV":
                print("Cost per day is $100")
                self.total=self.days*100
                print("Total Cost: "+str(self.total))
            
        else:
            print("Requested car not available")
        

    # def addcar(self):
    #     pass


# class Customer:

#     # def requestCar(self):
#     #     self.entry=input("Enter the name of the car you would like to rent: ")
#     #     self.days=input("Enter the nnumber of days: ")
#     #     return self.entry

#     def returnCar(self):
#         pass


car=Car(['HatchBack','Sedan','SUV'])
while True:
    print("********Car Rental System********")
    print("1. Display Available Cars")
    print("2. Rent Car")
    print("3. Exit")
    userChoice=int(input("Enter the choice: "))
    if userChoice is 1:
        car.displayAvailableCars()
    elif userChoice is 2:
        car.lendCar()
    elif userChoice is 3:
        quit()
# customer=Customer()