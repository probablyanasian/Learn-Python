#!/usr/bin/env python3
import os
import sys
import string
from subprocess import Popen, PIPE, STDOUT
from secrets import randbits, choice

# Get the path this file is in
path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), 'Ch1-final.py')  # Be sure to specify which practice problem
# Make dict for query strings
queries = {}
queryNum = 0
# Edit according to number of inputs sent
letterList = list(string.ascii_uppercase)[:1]
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

valid_chars = f'{string.digits}{string.ascii_letters}'
selection_chars = f'{valid_chars}{string.punctuation}'


def text_gen(letters):
    return (''.join(choice(selection_chars) for _ in range(letters)))


correct = True
for loopNum in range(25):
    # Open the subprocess
    p = Popen([sys.executable, '-u', path],
              stdout=PIPE, stdin=PIPE, stderr=PIPE, encoding='utf-8')

    ### GENERATE INPUTS ###

    inputA = text_gen(randbits(10))
    if loopNum == 0:
        inputA = 'Hello, world, test test 123.'

    ### DONE GENERATING ###

    # Send in my test inputs, and get the error back as well
    test_output, test_error = p.communicate(
        input=f'{inputA}')  # Modify to vary input amounts
    # Make sure the subprocess closed before continuing
    p.wait()

    ### FIND EXPECTED OUTPUT ####
    expected = ''
    expec_dict = {}
    inputA.strip()
    for i in inputA:
        expec_dict[i] = inputA.count(i)
        # Increase speed slightly, when there's multiple of the same char.
        inputA.strip(i)
    for letter in sorted(expec_dict):
        if letter in valid_chars:
            stars = '*'*expec_dict[letter]
            expected += f'{letter}: {stars}\n'

    ### DONE FINDING EXPECTED OUTPUT ###

    # Remove the query string(s)
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

        # Shorten response output default 80 now. Also replace newlines to be space \n space
        test_output = test_output.replace('\n', ' \n ')
        expected = expected.replace('\n', ' \n ')
        test_output = (
            test_output[:80] + (test_output[80:] and '..'))

        expected = (
            expected[:80] + (expected[80:] and '..'))

        # Tell user how it failed
        print(f'Input A: {inputA}')
        print(
            'Truncated to show first 80 characters, if present, newlines replaced as \' \\n \'.')
        print(f'Outputted: {repr(test_output)}')
        print(f'Expected:  {repr(expected)}')
        break

if correct:
    print('Congrats!, you did it correctly.')
