
"""
courses = ['Maths', 'Physics', 'Chem.', 'Comp.Sci']
print(len(courses))
print(courses)
"""
##################
"""
courses = ['Maths', 'Physics', 'Chem.', 'Comp.Sci']
print(courses[-2])
"""
##################
"""
courses = ['Maths', 'Physics', 'Chem.', 'Comp.Sci']

print(courses[2:3])
"""
####################
"""
courses = ['Maths', 'Physics', 'Chem.', 'Comp.Sci']
courses.append('Commerce')
print(courses)
"""
######################
"""
courses = ['Maths', 'Physics', 'Chem.', 'Comp.Sci']
popped = courses.pop()
print(courses)
print('popped: {}'.format(popped))
"""
#########################
"""
courses = ['Maths', 'Physics', 'Chem.', 'Comp.Sci']
courses.reverse()
print(courses)
"""
############################
"""
science = ['Maths', 'Physics', 'Chem.']
arts = ['History', 'Georgraphy']
science.insert(0,arts)
print(science)
"""
##########################
"""
science = ['Maths', 'Physics', 'Chem.']
arts = ['History', 'Georgraphy']

science.extend(arts)
print(science)
"""
###########################
""""
science = ['Maths', 'Physics', 'Chem.']
science.insert(1,'Comp.Sci')
print(science)
"""
##############################
"""
science = ['Maths', 'Physics', 'Chem.']
science.remove('Chem.')
print(science)
"""
#############################
"""
courses = ['Maths', 'Physics', 'Chem.']
courses.sort()
print(courses)
"""
#################################
"""
courses = ['Maths', 'Physics', 'Chem.']
courses.sort(reverse = True)
print(courses)
"""
#################################
"""
courses = ['Maths', 'Physics', 'Chem.']
print(sorted(courses)) # sorted list returned.

print(courses) # original list will remain same
"""
#################################
"""
list_1 = [1,2,3,4,5] # list is mutable
list_2 = list_1

list_1.append(100)
print(list_1)
print(list_2)
"""
################################
"""
fruits = ['Grapes', 'Apples', 'Oranges', 'Bananas']
for index, fruit in enumerate(fruits):
      print(index, fruit)
"""
################################
######## tuple
#################################
"""
student = ('Satish', 40, 120000.00)
print(student)
"""
###################################
"""
fruits = {'grapes', 'apples', 'bananas'}
print(type(fruits))
print(fruits)
"""
###################################
"""
fruits = {'grapes', 'apples', 'bananas', 'grapes'}
print(type(fruits))
print(fruits)
"""
##################################
"""
fruits = {'grapes', 'apples', 'bananas'}
print(fruits)
fruits.add('mangoes')
fruits.add('apples')
print(fruits)
"""
####################################
"""
a = {3,6,9,11}
b = {1,2,3,4,6}
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
"""
####################################
"""
list_1 = []
print(type(list_1))
list_2 = list()
print(type(list_2))
tup_1 = ()
print(type(tup_1))
tup_2 = tuple()
print(type(tup_2))
set_1 = set()
print(type(set_1))
dict_1 = {}
print(type(dict_1))
"""
























































































































































































