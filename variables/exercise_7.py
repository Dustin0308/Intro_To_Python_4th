# What happens when you run the following code? Why?

NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)




# My Answer:

# It will print a greeting 3 times to Victor and then a greeting 3 times to Nina. This happens 
# because the code initialized the value of Victor to NAME and then reassigned NAME to Nina 
# after printing the 3 greetings to Victor. Since it was then reassigned, NAME now points to Nina
# at a different location in memory, not Victor. It should be noted that 'NAME' is a constant 
# and we should not reassign constants, so the software engineer should have used a regular
# variable instead if they wanted to reassign name at a later date. It is bad practice to 
# reassign constants.






# Launch School's Answer:

# The program first greets Victor 3 times. It then greets Nina 3 times.

# Unfortunately, Python doesn't have real constants. There's no way to prevent the reassignment of 
# NAME. If this faux-constant really needs to be changed, you should use a regular variable instead:

name = 'Victor'
print('Good Morning, ' + name)
print('Good Afternoon, ' + name)
print('Good Evening, ' + name)

name = 'Nina'
print('Good Morning, ' + name)
print('Good Afternoon, ' + name)
print('Good Evening, ' + name)
