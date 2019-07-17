#!/usr/bin/env python3
import os
import sys
import string
from subprocess import Popen, PIPE, STDOUT
from secrets import randbits

# Get the path this file is in
path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '5-practice.py')

# Make dict for query strings
queries = {}
queryNum = 0
letterList = list(string.ascii_uppercase)[:2]
# This time, 2 letters
for letter in letterList:
    # Open the process
    p = Popen([sys.executable, '-u', path],
              stdout=PIPE, stdin=PIPE, stderr=PIPE, encoding='utf-8')
    blank_input = ''
    if queryNum != 0:
        for _ in range(queryNum):
            blank_input += '0\n'
    # Get the query string
    output_str = p.communicate(input=blank_input)[0]
    # Strip previous query strings
    for indexNum in range(len(queries)):
        output_str = output_str.replace(
            queries[letterList[indexNum]], '', 1)
    queries[letter] = output_str
    # Make sure the process closes
    p.wait()
    queryNum += 1

correct = True
for _ in range(25):
    # Open the subprocess
    p = Popen([sys.executable, '-u', path],
              stdout=PIPE, stdin=PIPE, stderr=PIPE, encoding='utf-8')

    ### GENERATE INPUTS ###

    # Generate my test inputs, randomly
    # mult 3 to increase probability of being greater than B
    inputA = randbits(10)*3
    inputB = randbits(5)
    proper_input = False
    while not proper_input:
        if inputB == 0 or inputA == 0:
            # Seperated further for more efficiency in compiler
            if inputB == 0:
                inputB = randbits(5)
            else:
                inputA = randbits(10)*3
        elif inputA == inputB:
            inputA += randbits(3)  # add an int 0-8
        elif inputA < inputB:
            inputA, inputB = inputB, inputA  # Swap, guarantees size
        else:
            proper_input = True

    ### DONE GENERATING ###

    # Send in my test inputs, and get the error back as well
    test_output, test_error = p.communicate(input=f'{inputA}\n{inputB}')
    # Make sure the subprocess closed before continuing
    p.wait()

    ### FIND EXPECTED OUTPUT ####
    expected = '\n'.join([str(num)
                          for num in range(inputA+1) if (num) % inputB != 0])
    ### DONE FINDING EXPECTED OUTPUT ###

    # Remove the query strings
    for indexNum in range(len(queries)):
        test_output = test_output.replace(
            queries[letterList[indexNum]], '', 1).strip()

    # Check the result
    if test_output == expected:
        pass
    # If there was an error raised
    elif test_error != '':
        print(f'Your program outputted the following error:\n{test_error}')
        break
    else:
        correct = False
        test_output = (
            test_output[:25] + (test_output[25:] and '..')).replace('\n', ' ')
        expected = (expected[:25] + (expected[25:]
                                     and '..')).replace('\n', ' ')
        # Tell user how it failed
        print(f'Input A: {inputA}    Input B: {inputB}')
        print('Truncated to show first 25 characters, also newlines replaced as spaces.')
        print(f'Outputted: {repr(test_output)}')
        print(f'Expected:  {repr(expected)}')
        break

if correct:
    print('Congrats!, you did it correctly.')
