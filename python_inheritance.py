class Person():
    def __init__(self,name):
        self.name=name
    
    def display_name(self):
        print(self.name)
    #by default person is not employed
    def isEmp(self):
        print(self.name,' is not employed !!')


#derived class
class Employee(Person):
    def isEmp1(self):
        print(self.name,' is employed !!')

emp=Person('Vikas')
emp.display_name()
emp.isEmp()
emp1=Employee('Varun')
emp1.display_name()
emp1.isEmp1()

