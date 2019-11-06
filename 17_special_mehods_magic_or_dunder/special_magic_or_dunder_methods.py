
class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@email.com'.format(first, last)

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


############## Driver code ################

emp_1 = Employee('Satish', 'Narra', 50000)
emp_2 = Employee('Nagesh', 'G', 60000)

#print(emp_1)
#print(repr(emp_1))
#print(str(emp_1))
#print(emp_1.__repr__())
#print(emp_1.__str__())

##print(1+2)
##print(int.__add__(1,2))
##print(str.__add__('a','b'))
##print('a' + 'b')

#print(emp_1 + emp_2)
print(len(emp_1))
























