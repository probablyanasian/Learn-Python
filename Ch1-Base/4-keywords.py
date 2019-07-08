# Keywords are reserved words in Python.
# keywords cannot be used as a variable name, function name or any other identifier.
# However they are reserved to do special functions
# Here are some keywords you will need to know for now.

# def funct():  ; defines a user defined function
# if (boolean):  ; checks if the argument is True or False, and if True, does the lines that are indented below it.
# and  ; And gate, requires both sides to be True to return True
# or  ; Or gate, requires only one side to be True to return True
# elif (boolean):  ; else if, like "if" but will run only when the "if" statement above it is False
# else:  ; runs when all the 'elif' and 'if' statements above it fail
# return(object)  ; returns the object and exits the function when ran
# pass  ; does nothing, used when the code expects a line

#This sample program returns what type argument_one is, as a string
def function_a(argument_one):
  #Check if the argument type is an int and not a string (obviously not possible, but here for demo)
  if (type(argument_one) == int) and (type(argument_one) != str):
    return('int')
  #If the argument is a string or a list
  elif (type(argument_one) == str) or (type(argument_one) == list) :
    print('string or list')
    #Now that we know it's either a string or a list check if it's a string
    if (type(argument_one) == str):
      #It's a string
      return('string')
    #Otherwise, it's a list, and return that
    else: return('list')
  #Since there's a pass statement here, the else statement isn't actually required
  #However it *is* here to show its purpose
  else:
    pass
  return('neither')

#Try it out, change the function's argument, then run it
print(function_a('replace me'))
