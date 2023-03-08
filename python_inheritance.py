#how to initialize constructor in base class
class Person():
    def __init__(self,name):
        self.name=name
    
    def display_name(self):
        print('Employee_name:',self.name)
    #by default person is not employed
    def isEmp(self):
        print(self.name,' is not employed !!')


#derived class child class
class Employee(Person):
    
    def __init__(self,emp_name,emp_id,salary,designation):
        self.emp_id=emp_id
        self.emp_salary=salary
        self.emp_designation=designation

        #calling constructor of base class
        #Person.__init__(self, emp_name) normal way but not preferred
        #we can use super keyword to call
        super().__init__(emp_name)

    def isEmp1(self):
        print(self.name,' is employed !!')
    
    def emp_Details(self):
        print('Employee Id:',self.emp_id,
        '\nEmployee Sal:',self.emp_salary,
        '\nEmployee Designation:',self.emp_designation)

# emp=Person('Vikas')
# emp.display_name()
# emp.isEmp()
# emp1=Employee('Varun')
# emp1.display_name()
# emp1.isEmp1()

emp1=Employee('Varun', 100, 10000, 'Data Engineer')
emp1.display_name()
emp1.emp_Details()
