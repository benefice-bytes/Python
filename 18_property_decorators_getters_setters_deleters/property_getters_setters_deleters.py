
class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')        
        self.first = None
        self.last = None
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    


############# Driver code ############

emp_1 = Employee('Nagesh', 'G')

#print(emp_1.fullname)
#print(emp_1.email)

emp_1.fullname = 'Nagesh Guntamukkala'
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.fullname)









