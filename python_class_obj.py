#how to create class 
class Emp:
    #constructor
    #it is mainly used for assignment of instance variable
    def __init__(self,name,salary):
        self.emp_name=name #instance variable
        self.emp_sal=salary #instance variable
    
    #method of class
    def display_Emp(self):
        print("Employee name:",self.emp_name,",","Employee salary:",self.emp_sal)

emp1 = Emp("Varun", 1000)
emp2 = Emp("Vishal", 1050)

emp1.display_Emp()
emp2.display_Emp()
