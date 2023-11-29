'''
Function is a block of code that you can always use over and over age

to initialize a function, start with the `def` keyword followed by the function name
'''


## Syntax


def function_name():
    # logic goes here
    print("something")


'''
You can pass parameter inside the curve brackets after the function_name

These parameter are like placeholders that you can always provide values for
'''


## Example - age converter

def age_calculator(name, age):
    age_in_days = age * 365
    age_in_months = age * 12
    return (f"{name} is {age_in_days} in days old and {age_in_months} in months") # return the logic


'''
We have a function that is converting a (placeholder) age to days and months

If you run the code, it will not do anything because the function is not called

Let's call it and pass value to the parameters
'''

print(age_calculator("Stephen", 25)) # pass the value in of the parameters


## Default value for parameter

def username(name = "Stephen"): # Pass `Stephen` as default value
    return print(name)


username() # Although we did not pass a value for the parameter but Stephen is still printed