class car:
    def __init__(self,name,color):
        self.car_name=name
        self.car_color=color
    def display_carDetails(self):
        print('Car name:',self.car_name,',','Car color:',self.car_color)
    
    @staticmethod
    def welComeMsg():
        print("Welcome Car")

#static method can be called directly without creating obj or instance of class 
#can be use Static methods are: Safe to use. Since static 
# methods cannot access the class or instance data, they cannot modify the class state. 
# This method cannot change the behavior or affect a class unexpectedly.
car.welComeMsg()
car1=car('BMW', 'Black')
car1.display_carDetails()

#Xyz company
class Emp:
    @staticmethod
    def isEmployeeOf():
        print("Employee of Xyz company")

Emp.isEmployeeOf()
