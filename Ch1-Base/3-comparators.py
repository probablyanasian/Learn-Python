# Comparators allows the program to compare two values.
# They return a boolean value, whether it's true or not.

# There are eight comparison operations:

# Less than
1 < 3  # True

# Less than or equal
1 <= 1  # True

# Greater than
3 > 2  # True

# Greater than or equal
2 >= 2  # True

# Equal to
'string' == 'string'  # True
1 == 1  # True
['a', 'b'] == ['a', 'b']  # True

# Not equal to
'this' != 'that'  # True
1 != 2  # True
['b', 'a'] != ['a', 'b'] #True

# init for demo below
a = ['a', 'b', 'c']
b = ['a', 'b', 'c']
c = a

# Identity ; Checks whether they are referring to the same object
a is b  # False
a is c  # True

# Negated identity ; Checks if they're not referring to the same object
a is not b  # True
a is not c  # False

# Try it out and take a look, print() out their values