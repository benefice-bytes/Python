"""
def hello_fun():
      pass

print(hello_fun)
print(hello_fun())
"""
################################
"""
def fun():
      print('Hello world')

fun()
"""
##############################
"""
def add(x, y):
      print(x+y)

add(10, 20)
"""
#############################
"""
def add(x, y):
      return x+y

print(add(10, 20))
"""
#############################
"""
def student_info(name, loc='india'):
      print('{0} is from {1}'.format(name, loc))

student_info('nagesh', 'china')
student_info('satish')
"""
##############################
"""
def student_info(name, age):
      print('{0} is {1} years old.'.format(name, age))

student_info('Satish', 40) # these positional args
student_info(age=40, name='nagesh') # keyword args
"""
##############################
"""
def student_info(*args, **kwargs):
      print(args)
      print(kwargs)

student_info(['Maths','Sci.','Stats'],name='Ram', age = 28)
"""
###############################
"""
def student_info(*args, **kwargs):
      print(args)
      print(kwargs)

courses = ['Maths', 'Science', 'Social']
info = {'name': 'Nagesh', 'age': 38}
student_info(*courses, **info)
"""






























































