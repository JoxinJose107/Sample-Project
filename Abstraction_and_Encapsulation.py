# Abstraction and Encapsulation

# Problem statement.
# Implemement the library management system that performs the following tasks:
    # 1) Customer should be able to display all the books available in the library
    # 2) Handle the process when customer requests to borrow a book.
    # 3) Update the library collection when customer returns a book.
'''
class => library
Layers of Abstraction => display available books, to lend a book, to add a book

class => Customer
Layers of Abstraction => request a book, return a book'''


class Library:
    def __init__(self,listOfBooks):
        self.originalLists=listOfBooks
        self.availableBooks=listOfBooks
    def displayAvailableBooks(self):
        print("*****Available Books*****")
        for book in self.availableBooks:
            print(book)
        print("************************")
    def lendBook(self,requestedBook):
        if requestedBook in self.availableBooks:
            self.availableBooks.remove(requestedBook)
            print("You have Successfully Borrowed the book!!")
        else:
            print("Requested book not available")
    def addBook(self,returnedBook):
        if returnedBook in self.originalLists:
            self.availableBooks.append(returnedBook)
            print("You have returned the book")
        else:
            for book in self.originalLists:
                print(book)
class Customer:
    def requestBook(self):
        self.book=input("Enter the book you would like to borrow: ")
        return self.book
    def returnBook(self):
        self.book=input("Enter the name of the book you want to return: ")
        return self.book
library=Library(['The Alchemist','Rich Dad Poor Dad','The Monk Who Sold His Ferrari'])
customer=Customer()
while True:
    print("**************LIBRARY MANAGEMENT SYSTEM***********")
    print("1. Display Available Books")
    print("2. Request for a Book")
    print("3. Return a Book")
    print("4. Exit")
    userChoice=int(input("Enter the choice: "))
    if userChoice is 1:
        library.displayAvailableBooks()
    elif userChoice is 2:
        requestedBook=customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice is 3:
        returnedBook=customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice is 4:
        quit()

    
