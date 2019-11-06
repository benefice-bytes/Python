class Employee:
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@company.com'.format(first, last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


############# Driver code 1 ###############

emp_1 = Employee('Satish', 'Narra', 60000)

emp_str_1 = 'Nagesh-Guntamukkala-75000'
emp_2 = Employee.from_string(emp_str_1)

print(emp_1.fullname())
print(emp_2.fullname())

##Employee.set_raise_amount(1.06)
##print(emp_1.raise_amount)
##print(emp_2.raise_amount)

##import datetime
##my_date = datetime.date(2019, 11, 9)
##print(Employee.is_workday(my_date))































        

        
