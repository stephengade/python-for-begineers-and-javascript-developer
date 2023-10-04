'''
Data types specify which kind of value a variable can hold, either text, number etc.
'''

# Numbers

'''
We have integers and float. Integers are WHOLE numbers while Float has decimal point
'''

age = 30 
balance = 50.6

# Strings

'''
Strings are sequence of characters such as text and it defined with either double or single quotation marks
'''

language = "Python"

# Boolean

'''
Boolean tells us is something is TRUE or FALSE
'''

Is_Python_Good = True

# Lists

'''
List is a collection of items, which can hold different data types. In JavaScript, we call it ARRAY. A list can be altered or changed.
'''

fruits = ["apple", "banana", "cherry"]


# Turples

'''
Just like LISTS, Turples are also collection of items but they are not mutable, that it, they can't be altered or changed.

There is not direct way to initialize something like Turple in JavaScript, but you can `freeze` a list to achieve the same purpose;

e.g: const turple_in_javacript = Object.freeze([1, 2, 3, 4, 5]);
'''

coordinates = (3.666, 4.55)

# Dictionaries

'''
Dictionaries are collections of key-value pairs where each key is UNIQUE. Dictionary is similar to JavaScript's Object but Objects have much larger capabilities
Check this thread for the differences: https://stackoverflow.com/questions/20987485/what-are-the-differences-between-python-dictionaries-vs-javascript-objects
'''

person = {
  "name": "Stephen Gbolagade",
  "age": 30
}


# Sets and Frozen sets

'''
Sets are unordered collections of unique items. They are initialize by {} or set() contructor with LIST or Turple. sets are Mutable

There is also `set` object in javascript ES6+ -> age_group = new set([10, 5, 9, 40, 58]).

There is no direct way to initialise frozenset in JavaScript but you can freeze the set to make it immutable
'''

age_group = {10, 5, 9, 40, 58} 
age_range = set([10, 5, 9, 40, 58])



# frozenset are immutable sets

age_interval = frozenset([10, 5, 9, 40, 58])