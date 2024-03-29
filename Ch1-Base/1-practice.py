# Try creating some variables
# Don't be discouraged if you need to look back
# Run this program to check

# ex. Store the word 'hello' inside of 'world'
# Replace None with the right value
world = 'hello'

# Delete the variable 'world'


# Store an integer inside of 'a'
a = None

# Store a string inside of 'b'
b = None

# Store a list inside of 'c'
c = None

# Store a tuple inside of 'd'
d = None

# Store a dict inside of 'e'
e = None

# Store a boolean inside of 'f'
f = None

# Store a set inside of 'g'
g = None


# Check algorithm
check = True
variables = [a, b, c, d, e, f, g]
var_name = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
types = [int, str, list, tuple, dict, bool, set]

# Check if the variable world still exists
if 'world' in globals():
    print('The variable \'world\' still exists')
    check = False

# Go through the variables, and check if they are the right type
for num in range(0, 6):
    if type(variables[num]) == types[num]:
        pass
    else:
        print('{0} is not a {1}'.format(var_name[num], types[num]))
        check = False

if check:
    print('Congrats, you finished the practice correctly')
