# There are 2 types of loops in python.
# The for loop and the while loop.

# Addtl. keywords
# continue  ; stops the current loop, and starts the next loop
# break  ; exit the current loop

# for iter in iterable ; loop a predetermined number of times
print('for loop 1')
for num in range(10):
    # requires code here
    print(num)  # prints 0, 1, ... 9

print('\n\n')  # Add 2 blank lines in between loops

print('for loop 2')
for num in range(10):
    if num == 5:
        continue
    print(num)  # prints 0, 1, ... 4, 6, ... 9
# for loops are useful for repetitive tasks.

print('\n\n')  # Add 2 blank lines in between loops

# while bool/condition ; also called a conditional loop, it will loop until boolean is false.
print('while loop 1')
loopnum = 0
while loopnum <= 9:
    # requires code here
    print(loopnum)  # prints 0, 1, ... 9
    loopnum += 1

# or, to achieve the same effect
print('while loop 2')
loopnum = 0
while True:
    print(loopnum)  # prints 0, 1, ... 9
    if loopnum >= 9:
        break
    loopnum += 1
# while loops are useful for repetitive tasks, but you don't know how long/many loops it will take to finish.
