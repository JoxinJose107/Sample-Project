

#***Abstract classs in python
from abc import ABCMeta, abstractmethod

class Shape:
    __metaclass__=ABCMeta
    @abstractmethod
    def area(self):
        return 0


class Square(Shape):
    side=4
    def area(self):
        print("Area of the square: "+str(self.side*self.side))

class Rectangle(Shape):
    length=3
    breadth=5
    def area(self):
        print("The area of of rectangle is: "+str(self.length*self.breadth))

square=Square()
rectangle=Rectangle()
square.area()
rectangle.area()