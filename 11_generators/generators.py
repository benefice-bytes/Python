# The following code, returns a list of square numbers.
"""
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


my_nums = square_numbers([1,2,3,4,5])
print (my_nums)
"""

#############################################################
# The above code can optimized in memory, by using generators
#############################################################
"""
def square_numbers(nums):
    for i in nums:
        yield(i*i) # yield returns one by one
    

my_nums = square_numbers([1,2,3,4,5])
#print (my_nums) # returns <generator object square_numbers at 0x03269300>
for num in my_nums:
    print(num)
"""

# The above code can be written in a simple way,
# but still it is not optimized in memory consumption, and speed
"""
my_nums = [x*x for x in [1,2,3,4,5]]
print(my_nums)
"""
