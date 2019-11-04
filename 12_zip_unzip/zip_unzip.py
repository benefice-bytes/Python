##name = ["Nagesh", "Satish", "JRam"]
##roll_no = [501, 502,503]
##marks = [90, 89, 78]
##
##mapped = zip(name, roll_no, marks)
##mapped = list(mapped)
##print(mapped)
############################
## unzip
############################

##name_1, roll_no_1,marks_1 = zip(*mapped)
##print(name_1)
##print(roll_no_1)
##print(marks_1)

fruits = ['apples', 'Bananas', 'Oranges']
price = [90.0, 85.90, 78.67]

for f, p in zip(fruits, price):
    print('{0} - {1}'.format(f,p))
