#!/usr/bin/env python3
import os
import sys
import string
import secrets
import random
import subprocess

# Get the path this file is in
path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '1-practice.py')

# Gen for letters
def text_gen(letters):
    return (''.join(secrets.choice(string.ascii_letters) for _ in range(letters)))

correct = True
for loopNum in range(1):

    ### GENERATE INPUTS ###
    expected = ''
    with open('practice.txt', 'r+') as practice_file:
        practice_file.truncate(0)
        to_read = random.randint(0, 45)
        column_to_read = random.randint(0, 50)
        practice_file.write(str(to_read)+' '+str(column_to_read)+'\n')
        for lines in range(random.randint(45, 70)):
            to_write = text_gen(random.randint(50, 65))+'\n'
            expected += to_write[column_to_read]
            practice_file.write(to_write)

    ### DONE GENERATING ###

    # Open the subprocess
    p = subprocess.run([sys.executable, '-u', path], encoding='utf-8')

    # Send in my test inputs, and get the error back as well
    test_error = p.stderr
    test_output = p.stdout

    # Make sure the subprocess closed before continuing

    ### FIND EXPECTED OUTPUT ####
    ### DONE FINDING EXPECTED OUTPUT ###

    # Check the result
    if test_output == expected:
        pass
    # If there was an error raised
    elif test_error != '' or None:
        print(f'Your program outputted the following error:\n{test_error}')
        break
    else:
        correct = False

        # Shorten response output
        test_output = (
            test_output[:80] + (test_output[80:] and '..')).replace('\n', ' ')
        solution = []

        expected_output = expected
        expected =  (
            expected_output[:80] + (expected_output[80:] and '..')).replace('\n', ' ')
        # Tell user how it failed
        print(
            'Truncated to show first 80 characters, if present newlines replaced as spaces.')
        print(f'Outputted: {test_output}')
        print(f'Expected:  {expected}')
        break

if correct:
    print('Congrats!, you did it correctly.')
