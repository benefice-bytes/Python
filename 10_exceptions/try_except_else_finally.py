#Scenarion 1
"""
try:
    f = open('exceptions.txt', 'r')
    contents = f.read()
    print(contents)
    f.close()
    var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

"""

#Scenario 2
"""
try:
    f = open('test_file.txt', 'r')
    #print(f.read())
    #f.close()
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print('Executing else...')
    print(f.read())
    f.close()
finally:
    print('Executing finally...')

"""
#Scenario 3
try:
    f = open('test_file.txt', 'r')
    if f.name == 'test_file.txt':
        raise Exception('file corrupted')  # manually raising exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print('Executing else...')
    print(f.read())
finally:
    f.close()
    print('Executing finally...')
