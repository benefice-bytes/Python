# install memory_profiler module
##########################################################
#### google: download memory_profiler python
#### extract copy memory_profiler to d:\python38\scripts>
#### d:\python38\scripts>pip install memory_profiler
##########################################################
# set path of memory_filer in system environment variables
# D:\Python38\Scripts\memory_profiler-0.55.0
##########################################################

import memory_profiler
import random
import time

names = ['Sowmya', 'Mounaa', 'Kaushee', 'Nazeer', 'Umar', 'Rajina']
majors = ['Arts', 'Engg.', 'Dance', 'Business', 'Astro', 'Agri']

print('Memory (Before): {0}Mb'.format(memory_profiler.memory_usage()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person


##### driver code #####
#t1 = time.time()
#people = people_list(1000000) # 1 million records
#t2 = time.time()

t1 = time.time()
people = people_generator(1000000) # 1 million records
t2 = time.time()

print('Memory (After): {0}Mb'.format(memory_profiler.memory_usage()))
print('Took {0} seconds.'.format(t2-t1))
