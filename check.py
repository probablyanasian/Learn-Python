#!/usr/bin/env python3
import os
import sys
import string
from subprocess import Popen, PIPE, STDOUT
from secrets import randbits

# Get the path this file is in
path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '-practice.py') # Be sure to specify which practice problem
# Make dict for query strings
queries = {}
queryNum = 0
letterList = list(string.ascii_uppercase)[:num_of_inputs] # Edit according to number of inputs sent
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
for loopNum in range(25):
    # Open the subprocess
    p = Popen([sys.executable, '-u', path],
              stdout=PIPE, stdin=PIPE, stderr=PIPE, encoding='utf-8')

    ### GENERATE INPUTS ###

    #Set up inputs here

    ### DONE GENERATING ###

    # Send in my test inputs, and get the error back as well
    test_output, test_error = p.communicate(input=f'{inputs}') #  Modify to vary input amounts
    # Make sure the subprocess closed before continuing
    p.wait()

    ### FIND EXPECTED OUTPUT ####
    
    # Find expected outputs here

    ### DONE FINDING EXPECTED OUTPUT ###

    # Remove the query string(s)
    for indexNum in range(len(queries)):
        test_output = test_output.replace(
            queries[letterList[indexNum]], '', 1).strip()

    # Check the result
    if test_output in expected:
        pass
    # If there was an error raised
    elif test_error != '':
        print(f'Your program outputted the following error:\n{test_error}')
        break
    else:
        correct = False

        # Shorten response output default 80 now. Also replace newlines to be spaces
        test_output = (
            test_output[:80] + (test_output[80:] and '..')).replace('\n', ' ')
        solution = []

        expected = (
            expected[:80] + (expected[80:] and '..')).replace('\n', ' ')

        # Tell user how it failed
        print(f'Input A: {inputA}')
        print(
            'Truncated to show first 80 characters, if present newlines replaced as spaces.')
        print(f'Outputted: {repr(test_output)}')
        print(f'Expected:  {repr(expected)}')
        break

if correct:
    print('Congrats!, you did it correctly.')
