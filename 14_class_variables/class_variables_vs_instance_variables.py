class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@company.com'.format(first,last)

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(first, last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


########## Driver code 1 ##########

##print(Employee.num_of_emps)
##emp_1 = Employee('Satish', 'Nara', 50000)
##emp_2 = Employee('Nagesh', 'Gunta', 60000)
##print(Employee.num_of_emps)
##
##print(emp_1.__dict__)
##print(emp_2.__dict__)
##print(Employee.__dict__)

########## Driver code 2 ##########


emp_1 = Employee('Satish', 'Nara', 50000)
emp_1.raise_amount = 1.06
emp_2 = Employee('Nagesh', 'Gunta', 60000)


print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.__dict__)














        
    
