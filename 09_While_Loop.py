'''
While loop is another control flow in programming and it is different from `For loops`

just like the keyword, it runs "while" the condition is still true
'''

## Example

number = 1

while number <= 10: # while number is less or equal to 10
    print(number)
    number += 1 



'''
 While loop can be used to handle a persistent program until a condition is met

 and example is if user age is not up to 18, tell the person he is not eligible

'''

# GAME - an age guessing game that gives the user 3 chances to guess the right age


min_age = 18
eligible = False
trials = 0


while not eligible and trials < 3:  # while user is not eligible
    user_age = 3 #int(input("What is your age: ")) # Let user enter their age
    trials+=1  # increment the trial each time the user is incorrect
    if user_age >= min_age:
          eligible = True
          print(f"{user_age} - You are eligible") # if the user is correct
    else:
         eligible = False
         print(f"{trials} out of 3 used: {'Trials over' if trials == 3 else 'Try again'}")



## Note - Infinite loop

'''
Always break out the loop when the condition is met to avoid infinite loop

You can either use the `break` keyword when a condition is met 

Or update check for truthy or falsy as used above.
'''

age = 18
  
while age:
     print(age)
     break # if this break keyword is not added, the while loop will keep running because the condition is always true



## Another instance 

while age:
     age += 1 # it will keep adding one to age (18)
     if age == 25:
          break  # stop when it gets to 25
     else:
          print(age) # print the result before it break

'''
If break is not use above, it will keep adding 1 until infinity
'''



# You can also use continue to skip here too

number = 12

while number:
     number += 1
     if number % 2 == 0:
          continue # skip all number divisible by 2
     elif number > 30:
          break # stop if age is greater than 30. i.e 31
     else:
          print(f"age is: {number}") # if all the conditions above are meant, print what you got
