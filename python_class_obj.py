#how to create class 
class Emp:

    emp_Count=0 #class variable
    #constructor
    #it is mainly used for assignment of instance variable
    def __init__(self,name,salary):
        self.emp_name=name #instance variable
        self.emp_sal=salary #instance variable
        Emp.emp_Count += 1
    #method of class
    def display_Emp(self):
        print("Employee name:",self.emp_name,",","Employee salary:",self.emp_sal)
    
    def display_EmpCount(self):
        print('Employee count:',Emp.emp_Count)

#difference between class variable and instance variable
emp1 = Emp("Varun", 1000)
emp1.display_Emp()
emp1.display_EmpCount()

emp2 = Emp("Vishal", 1050)
emp2.display_Emp()
emp2.display_EmpCount()

#count does not increase as it looks individually to the object
emp1.display_EmpCount()
emp2.display_EmpCount()


