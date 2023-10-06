'''
Turples are like collections of items, just like Python's list or JavaScript's array

But Turples are not mutable, that is you can not modify it which is equivalent to when you freeze an object in Javascript
'''

counts = (1, 2, 3, 4, 5) # or just 1, 2, 3, 4, 5

# Accessing

'''
You access each item based on their index, just like list... remember, indices start from 0
'''

counts[1] # will return 2

# Other operations on tuples

# counts * n will duplicate counts by n-times

counts * 3 # will return (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

3 in counts # will check if there is 3 in the typle and return True or False

# You can also merge multiple turples together by concatenation

counts_2 = 7,8,9,10,11

counts + counts_2 # will return (1, 2, 3, 4, 5, 7, 8, 9, 10, 11)

