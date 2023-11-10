'''
Operators are used in programming to manipulate variables and values, and to process data in the code.

There are 7 distinct operators in Python, which is also the same for other programming languages like JavaScript
'''

## Arithmetic Operators

'''
Are used to perform basic mathematical operation such as:

Addition (+), Subtraction (-), Multiplication (*), Division (/), Floor Division (//), Exponential (**), Modulus (%)
'''

# Modulus returns the remainder

10 % 3       # will return 1


# Floor Division will return the nearest whole number

10 // 3     # will return 3 instead of 3.3333




## Comparison Operators

'Are used to compare two values and it return True/False'

4 == 2      # means "Is 4 the SAME as 2?" the answer will be False
4 != 2      # means "Is 4 NOT THE SAME as 2?" the answer will be True
4 < 2       # means "Is 4 LESS THAN 2?" the answer will be False
4 > 2      # means "Is 4 GREATER THAN 2?" the answer will be True
4 >= 2      # means "Is 4 GREATER THAN or EQUAL to 2?" the answer will be True. Tho not equal to, but the condition `Greater than` is met
4 <= 2      # means "Is LESS THAN or EQUAL to 2?" the answer will be False



## Assignment Operators

'''
Are used to assign values. 

We have one standard assignment operation which is the `=` sign.

But we can combine arithmetic operators with it to give us more operators
'''

age =  10      # It assign value of 10 to variable `age`
age+=1         # Means `age + 1 = 11`. It grab the previous age value and add 1 to it, then finally return the result. 
age-=1         # Means `age - 1 = 9`. It grab the previous age value and subtract 1 to it, then finally return the result. 
age*=2         # Means `age * 2 = 20`. It grab the previous age value and multiply it by 2, then finally return the result. 
age**=2        # Means `age raised to power 2 = 100`. It grab the previous age value and squared it, then finally return the result. 
age%=2        # Means `age % 2 = 0`.




## Logical Operators

'''
Are used to perform logication operations.

There are `and`, `is`, `not` logical operators
'''

# For AND 

'''
They check from left to right for truthy or falsy. i.e If something is true or not

Note this:
- All numbers except 0 are True
- All strings are True unless it's empty string
- List, Dictionary, Turples etc are True unless they are empty
- None is False


ALSO

- If both values checked are True, the second one will be returned
- If both values are False, the first one will be returned/
- If the first value is False, it will return it.


Remember this table from your high school

T F = F
F T = F
T T = T
F F = F

'''


6 and 5       # 5 will be returned because both are True
0 and 5       # 0 will be returned because both are True



# for IS - It is used for Identity check

'''
Compares two object if they reference to the same object in memory, not comparing of VALUES

The `==` operator is used to check or compares value
'''

x = 5
y = 5

z = x

x is y      # False will be returned. Because x not the same as y. we compare identity not Value
x is z      # True will be returned because we have made the identity of x to be the same as z




# for NOT - It is used for Identity check

'''
not is used to negate. for instance, it changes true to false and vice versa

'''

Food =  True

not Food # returns False

not not Food # returns True because the first not, change it to false, the second not change it back to True




## Identity Operators

'''
Just like the logical operators, Identity operators are used to compared value stored in Memory. 

We have is `and` `is not`
'''

Food is True     # will return True
Food is not True  # will return False because Food is True



## Membership

'''
Used to check if a value is a member of a sequence

We have in, not in
'''

array = [1, 2, 3, 4, 5, 6]

2 in array                   # will return True because there is 2 in the sequence
3 not in array               # will return False because there is 3 in the sequence



## Bitwise operators

'''
Used for operation on Binary representations of numbers.

Bitwise is a little bit complicated, I have a technical article that explains it

Read here: https://dev.to/stephengade/mastering-bitwise-operations-a-simplified-guide-2031
'''