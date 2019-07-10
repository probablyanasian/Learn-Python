# This sample program returns if argument_one is a integer, string, or a list; as a string
# Keep in mind that this was written for demonstration and not for efficiency.
def function_a(argument_one):

  #Check if the argument type is an int and not a string.
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

  #Since this else statement isn't doing anything, it isn't actually required
  #However it *is* here to show usage.
  else:
    pass
  # It's neither a integer, string, or a list
  return('neither')

#Try it out, change the function's argument, then run it
print(function_a('replace me'))