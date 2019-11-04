"""
student = {'name': 'Kishore', 'age':33, 'courses': ['C++', 'Python','MFC']}
print(student)
print(student['name'])
#print(student['location'])
print(student.get('location', 'not found'))
"""
#############################
"""
student = {'name': 'Kishore', 'age':33, 'courses': ['C++', 'Python','MFC']}
student['age'] = 23
print(student)
"""
##############################
"""
student = {'name': 'Kishore', 'age':33, 'courses': ['C++', 'Python','MFC']}
student.update({'name':'Prakash', 'age':32})
print(student)
"""
##############################
"""
student = {'name': 'Kishore', 'age':33, 'courses': ['C++', 'Python','MFC']}
student.pop('age')
print(student)

courses = student.pop('courses')
print(student)
print(courses)
"""
##############################
"""
student = {'name': 'Kishore', 'age':33, 'courses': ['C++', 'Python','MFC']}
print(len(student))
"""
#############################
"""
student = {'name': 'Kishore', 'age':33, 'courses': ['C++', 'Python','MFC']}
print(student.keys())
print(student.values())
"""
##############################
"""
student = {'name': 'Kishore', 'age':33, 'courses': ['C++', 'Python','MFC']}

for key, value in student.items():
      print('{0} - {1}'.format(key, value))
"""





















































      


