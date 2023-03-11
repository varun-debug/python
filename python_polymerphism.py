#function overriding in python
from math import pi
class Shape:
    def __init__(self,name):
        self.name=name
    
    def area(self):
        pass

    def whichShape(self):
        print(self.name)

class square(Shape):
    def __init__(self, name, length):
        super().__init__(name)
        self.sideLength=length
    
    def area(self):
        print(self.sideLength * self.sideLength)

    def fact(self):
        print('All sides are equal and all angles are 90 degree')

class circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius=radius
    
    def area(self):
        print(pi *(self.radius ** 2) )

    def fact(self):
        print('Circle is 360 degree')

sq = square('Square', 5)
cr = circle('Circle', 5)
sq.whichShape()
cr.whichShape()
sq.area()
cr.area()
sq.fact()
cr.fact()
