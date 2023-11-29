'''
Control flow in programming is refers to the order in which instruction are executed.

And to achieve this, the `if`, `else` statements are used. 

This statements tell the program what and what to do at a particular instance
'''

## The syntax



condition_is_met = True   # There must be a condition to check for

if condition_is_met:
    x = "do something"
else:
   x = "oh condition is not met, do this otherwise"



## Example

'''
Let's say we have a club house that only people aged 18 years and above are allowed,

we can achieve that by checking for the condition and doing something if the condition is met
'''

age = 18

if age >= 18:
    text = "You can enter this club"
else:
    text = "You are too young to enter this club"


## Note - The identation is very important, Python care for it unlike JavaScript

'''
You can also nest multiplible if-else statements.

Let's say in the club, there are seperate sections for Male and Female, you can check that
'''

age = 18
gender = "male"

if age >= 18:
    if gender == "male":
        text = "You are welcome, go to male section"
    elif gender == "female": #note the use of elif
        text = "You are welcome, go to female section"
    else:
        text = "Okay, welcome, go to the receptionist for direction"
else:
    text = "You are too young to enter this club"


'''
In that program, we first of all check if the person is 18 or above

If yes, we check again if the person is male or female

If Yes, we display a message respectively AND If No, we direct the person to the receptionist

If the person is not up to 18, we tell the person that he/she is too young

'''
