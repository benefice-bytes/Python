class Employee:
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@company.com'.format(first, last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())
        
############# Driver code ############

dev_1 = Developer('Satish', 'Narra', 50000, 'Python')
dev_2 = Developer('Nagesh', 'G', 60000, 'Visual C++')

##print(dev_1.email)
##print(dev_2.email)

##print(help(Developer))

##print(dev_1.pay)
##dev_1.apply_raise()
##print(dev_1.pay)

##print(dev_1.email)
##print(dev_1.prog_lang)

mgr_1 = Manager('Nazeer', 'Shaik', 90000, [dev_1])
##print(mgr_1.email)
##
##mgr_1.add_emp(dev_2)
##mgr_1.remove_emp(dev_1)
##mgr_1.print_emps()

#print(isinstance(mgr_1, Employee))
print(issubclass(Developer, Employee))













