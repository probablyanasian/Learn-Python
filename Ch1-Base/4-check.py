#!/usr/bin/env python3
import os
import sys
import string
from subprocess import Popen, PIPE, STDOUT
from secrets import randbits

# Get the path this file is in
path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '4-practice.py')

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
for cur_test in range(25):
    # Open the subprocess
    p = Popen([sys.executable, '-u', path],
              stdout=PIPE, stdin=PIPE, stderr=PIPE, encoding='utf-8')

    # Generate my test inputs, randomly
    inputA = str(randbits(10))
    inputB = str(randbits(10))

    # Since it's hard to generate an equal scenario randomly with 10 bits
    if (cur_test % 5) == 0:
        # Force an equal scenario
        inputA = inputB

    # Send in my test inputs, and get the error as well
    test_output, test_error = p.communicate(input=f'{inputA}\n{inputB}')
    # Make sure the subprocess closed before continuing
    p.wait()
    # Find the expected output
    if inputB == inputA:
        expected = 'equal'
    elif inputB > inputA:
        expected = 'greater than'
    elif inputB < inputA:
        expected = 'less than'

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
        correct = False
        break
    else:
        correct = False
        # Tell user how it failed
        print(f'Input A: {inputA}    Input B: {inputB}')
        print(f'Outputted: {test_output}')
        print(f'Expected: {expected}')
        break

if correct:
    print('Congrats!, you did it correctly.')
