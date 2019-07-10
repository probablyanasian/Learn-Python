# Keywords are reserved words in Python.
# keywords cannot be used as a variable name, function name or any other identifier.
# However they are reserved to do special functions
# Here are some keywords you will need to know for now.

# def funct(arg1, arg2, ...):  ; defines a user defined function (doesn't require an argument)
def function():

    # return(object)  ; returns the object and exits the function when ran
    return(None)  # Has to be in a function

# pass  ; does nothing, used as a placeholder when the code expects something
# if (boolean):  ; checks if the argument is True or False, and if True, does the lines that are indented below it.
if(True):
    pass
# and  ; And gate, requires both sides to be True to return True
if (1 == 1) and True:
    pass
# or  ; Or gate, requires only one side to be True to return True
if (2 == 2) or False:
    pass
# elif (boolean):  ; else if, like "if" but will run only when the "if" statement above it is False
elif True:
    pass
# else:  ; runs when all the 'elif' and 'if' statements above it fail
else:
    pass
