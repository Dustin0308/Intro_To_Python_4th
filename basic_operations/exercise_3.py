# What does the following code do? Why?

print('5' + '10')







# My Answer:

# It will concatenate the strings '5' and '10' and will print out 510. This happens because when
# you use addition on two strings, it combines those two strings and returns a new string. It does 
# not recognize them as integers, but as strings. If you wanted to perform numeric addition to the 
# strings, you must complete a type conversion on the strings to integers or floats like so:

print(int('5') + int('10')) # 15






# Launch School's Answer: 

# The code prints 510. When used with string operands, + performs concatenation and returns a new 
# string. We've merely joined '5' and '10' to produce '510'.
