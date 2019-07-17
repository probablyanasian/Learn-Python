# A built-in in Python are some functions that are always available

# Some definitions first
# iterable: a countable object
# generator : a function that generates an iterable

#Some basic ones are shown here:
# Try running the file

# input() ; Reads an input from the terminal 
# This returns a string, but for the next few practices, don't convert the inputs to a different type.
user_input = input("Enter something: ")

# print() ; Prints something out onto the terminal.
print(user_input) # Whatever you inputted

# list(iterable) ; Creates a list, with the iterables given
a_list = list('Python')
print(a_list) # ['P', 'y', 't', 'h', 'o', 'n']

# len(object) ; Returns the length (number of objects) in an object
len(a_list) # 6

# type(object) ; Returns the type of the object
print(type(a_list)) # <class 'list'>

# range(start, stop) ; Creates a generator with the numbers from start to (stop-1)
a_range = range(0, 5)
print(list(a_range)) # [0, 1, 2, 3, 4]

# slice(start, stop, step) == a_list[start:stop:step] == a_list[slice(start,stop,step)]
# Returns a section of an iterable
print(a_list[1:5]) # ['y', 't', 'h', 'o']
print(a_list[slice(-5,-2)]) # ['y', 't', 'h']

# A helpful chart:
#                 +---+---+---+---+---+---+
#                 | P | y | t | h | o | n |
#                 +---+---+---+---+---+---+
# Slice position: 0   1   2   3   4   5   6
# Neg Slice Pos: -6  -5  -4  -3  -2  -1
# Index position:   0   1   2   3   4   5
# Neg Index Pos:   -5  -4  -3  -3  -2  -1

# Further Reading: https://docs.python.org/3/library/functions.html