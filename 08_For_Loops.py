'''
`For` Loops help you iterate over items and execute a certain command on each of the item

The items can be inform of a list, turple, dictionary or even a string


when using `for loop`, what you are saying is: for each of the item, do this
'''


## Example

item = "python"

for i in item:
    print(i)

# Expected result

'''
p
y
t
h
o
n
'''


priceLists = [100, 150, 300]

for price in priceLists:
    multipliedPrice = price * 2  # multiply each price by 2
   



## using `break`

'''
For loop will iterates over the items, run and return the logic on each item

But you can break away from it when a condition is meants
'''

for price in priceLists:
    totalPrice = price + 50
    if totalPrice > 200: #chekc if total price is greater than 200
        break 
    print(totalPrice) # only 150 and 200 will be printed



## using `continue`

'''
Continue let's you skip some items during the loopand continue on the next one

Unlike Break that will terminate the operation totally

'''

for price in priceLists:
    if price < 200:
        continue # skip the price below 200
    print(f"continue: {price}") 



# Use Break and continue together


for price in priceLists:
    addedPrice = price + 50
    if addedPrice > 300:
        break # stop at 300 or below
    if addedPrice == 150:
        continue # then remove any price that's 150
    print(f"addednumber: {addedPrice}")