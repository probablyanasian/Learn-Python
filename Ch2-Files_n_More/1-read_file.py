# Reading and writing to and from files is important
# But let's just talk about reading for now.

# Opening a file
# open('file', <type, endcoding... >)
# Types can be:
# r  ; read
# w  ; write
# a  ; append only
# r+ ; read and write
# b  ; binary file

# There are two ways to open a file
# First way
with open('example.txt', 'r+') as a_file:
    pass

# Second way
a_file = open('example.txt', 'r+')
a_file.close() # If you open this way, you should always close when done using it.

# This automatically closes the file for you when you after you de-indent
chars = 10

a_file = open('example.txt', 'r+')
# Reading a file, note that they continue off where the previous one stopped.
a_file.read(chars) #read a specific amount of characters
a_file.readline() # read until a newline char or EOF char