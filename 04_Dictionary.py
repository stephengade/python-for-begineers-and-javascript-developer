'''
Dictionaries in Python are used to stored data in key-value pair.

Although a dictionary look like JSON but they are different.

JSON is a standard for transfering data from one system to another
while DICTIONARY is a build-in data structure in Python and it is mostly used internally for data manipulation
'''

# Example 

profile = {'name': 'Stephen', 'age': 30, 'country': 'Nigeria'} # name, age, country are keys 

# To access the values

'''
You can access the value by either using .get() method or the square bracket `[]` and pass the key to get the value
'''

profile.get("name") # returns Stephen
profile['country'] # returns Nigeria

profile.items() # will return both key and pairs in an array
profile.values() # will return an array of values
profile.keys()  # will return an array of keys

# Modifying

'''
Dictionaries are mutable. Therefore, it is possible to change, remove and even delete elements from them
'''

profile["job"] = "Frontend developer" # Will add a new key-pair `"job": "Frontend Engineer"` to the profile
profile["age"] = 66 # Will change the age from 30 to 66
profile.pop("country") # will remove country from the dictionary, both key and pair
del profile["age"]  # will remove cage from the dictionary, both key and pair

# Merging two dictionaries

'''
It it possible to add muliple dictionaries together.
'''

grades = {"English": "B", "Maths": "A", "Python": "C"}

# you can add `grades` to `profile` above using update() method or `**`

profile.update(grades) # profile is now updated with grades. Note, this modifies the original profile, no new dictionary is returned

new_profile = {**profile, **grades} # new_profile has all the items from profile and grades. This returns a new dictionary

