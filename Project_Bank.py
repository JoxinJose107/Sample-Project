
#**Banking system  =Mini Project
#Problem Statement
#1) giving a prompt to the user asking if they wish to start a new savings account or access an existing account.
#2)if the user would like to create a new account, accept their name and initial deposit, and create a 5 digit random number and make it  as the account number of their new savings account.
#3)If they are accessing an existing account,accept their name and account number to validate the user, and give them options to withdraw, deposit or display their available balance.


from abc import ABCMeta,abstractmethod
from random import randint
class Account:
    __metaclass__=ABCMeta

    @abstractmethod
    def createAccount(self):
        return 0
    @abstractmethod
    def authenticate(self):
        return 0
    @abstractmethod
    def withdraw(self):
        return 0
    @abstractmethod
    def deposit(self):
        return 0
    @abstractmethod
    def displayAvailableBalance(self):
        return 0

class SavingsAccount(Account):


    def __init__(self):
        #[key][0] => name, [key][1] => Balance
        self.savingsAccounts={}
    
    def createAccount(self,name,initialDeposit):
        
        self.accountNumber=randint(10000,99999)
        self.savingsAccounts[self.accountNumber]=[name,initialDeposit]
        print("Your account has been successfully created, Account number is : ",self.accountNumber)

    def authenticate(self,name,accountNumber):
        if accountNumber in self.savingsAccounts.keys():
            if self.savingsAccounts[accountNumber][0]==name:
                print("Authentication Successfull!!")
                self.accountNumber=accountNumber
            else:
                print("Authentication failed")
                return False
        else:
            print("Authentication Failed")
            return False
        
    def withdraw(self,withdrawAmount):
        if withdrawAmount > self.savingsAccounts[self.accountNumber][1]:
            print("Insufficient Balance")
        else:
            self.savingsAccounts[self.accountNumber][1] -= withdrawAmount
            print("Amount Successfully Withdrawn")
            self.displayAvailableBalance()
        
    def deposit(self,depositAmount):
        self.savingsAccounts[self.accountNumber][1] += depositAmount
        print("Amount Successfully deposited")
        self.displayAvailableBalance()

    def displayAvailableBalance(self):
        print("Available Balance is : ",self.savingsAccounts[self.accountNumber][1])


savingsaccount=SavingsAccount() 

while True:
    print("1. Create new Account")
    print("2. Access an Existing Account")
    print("3. Exit")
    userChoice=int(input("Enter your choice: "))
    if userChoice is 1:
        name=input("Enter the name: ")
        initialDeposit=int(input("Enter the initial Deposit"))
        savingsaccount.createAccount(name,initialDeposit)
    elif userChoice is 2:
        name=input("Enter the name: ")
        accountNumber=int(input("Enter the account number"))
        authenticationStatus = savingsaccount.authenticate(name,accountNumber)
        if authenticationStatus is True:
            while True:
                print("1. Withdraw the money")
                print("2. Deposit the money")
                print("3. Display available balance")
                print("4. Go back to the previous menu")
                userChoice=int(input("Enter Your Choice"))
                if userChoice is 1:
                    withdrawAmount=int(input("Enter the withdrawal amount"))
                    savingsaccount.withdraw(withdrawAmount)
                elif userChoice is 2:
                    depositAmount=int(input("Enter the deposit amount"))
                    savingsaccount.deposit(depositAmount)
                elif userChoice is 3:
                    savingsaccount.displayAvailableBalance()
                elif userChoice is 4:
                    break
    elif userChoice is 3:
        quit


        
    


