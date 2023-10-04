'''
List is a collection of items in `[]`
'''

# for example

animals = ["Cat", "Dog", "Elephant", "Lion", "Monkey"]


# Accessing the items by Index. 
'''
Note that Python is ZERO index like javaScript meaning you start counting from 0,1,2... etc
'''


animals[0] #The first item, Cat
animals[2] #The Third item, Elephant
animals[-1] #The last item, Monkey
animals[-2] #The second-to-last item, Lion

# Slicing list

'''
You can select an item in list by index, what if you want to select mutiple items that follows each other? you can slice them.

For instance item[1:5] means start selecting from item with index 1 and stop at index 4.... The last item is not picked in slicing
'''

animals[1:4] # Dog, Elephant, Lion


# Modifying List

'''
Because LISTS are mutable, you can CHANGE, ADD or REMOVE items to/from it.
'''

# changing - You can change an item by selecting its index and assign a new value to it

animals[1] = "Zebra" # Our new list of animals becomes `Cat, Zebra, Elephant", Lion", Monkey`

# adding - You can add an item to the end of the list using `append`

animals.append("Gorilla") #`Cat, Zebra, Elephant", Lion", Monkey, Gorilla`
animals.extend(["Panda", "Rats", "Hippo"]) # Add multiple items to the list at once
animals.insert(2, "Panther") # Insert Panther at index of 2

# removing

animals.pop(3) # will remove item with index of 3 - `Lion`
del animals[2] # will remove item with index of 2 - `Elephant`
animals.remove("Cat") # Will look for Cat in the list and remove it (Case sensitive)


# LIST METHODS

'''
Methods are built-in functions that you can run to perform a particular functions
'''

len(animals) # How many items do you have in your list. JavaScript will use `list.length`
sorted(animals) # preserve the original list and return a modified sorted list
animals.sort() # sort the original list and return None


# COPYING

animals.copy() # Will return another shallow copy of animals. Same as the spread operator `...` in JavaScript


# ITERATING OR LOOPING

'''
Right now, if you print animals, it will return ['Gorilla', 'Hippo', 'Monkey', 'Panda', 'Rats', 'Zebra']

But what if you want to render each list independently?

in JavaScript, we can use for loop or the new ES6 syntax, list.map, in Python we simply use the `for loop`
'''

for item in animals:
    print(item)

'''
RESULT is:

Gorilla
Hippo
Monkey
Panda
Rats
Zebra
'''