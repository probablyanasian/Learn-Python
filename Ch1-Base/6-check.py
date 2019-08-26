#!/usr/bin/env python3
import os
import sys
import string
from subprocess import Popen, PIPE, STDOUT
from secrets import randbits

# Get the path this file is in
path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '6-practice.py')

# Make dict for query strings
queries = {}
queryNum = 0
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

correct = True
for loopNum in range(25):
    # Open the subprocess
    p = Popen([sys.executable, '-u', path],
              stdout=PIPE, stdin=PIPE, stderr=PIPE, encoding='utf-8')

    ### GENERATE INPUTS ###

    # Generate my test inputs, randomly
    inputA = randbits(10)

    # Force a small test first
    if loopNum == 0:
        inputA = 12
    ### DONE GENERATING ###

    # Send in my test inputs, and get the error back as well
    test_output, test_error = p.communicate(input=f'{inputA}')
    # Make sure the subprocess closed before continuing
    p.wait()

    ### FIND EXPECTED OUTPUT ####
    expected = []
    fibb = [1, 1]
    for term in range(inputA-2):
        fibb.append(fibb[term]+fibb[term+1])
    sol_A = fibb
    sol_B = [str(x) for x in fibb]
    sol_C = '\n'.join([str(x) for x in fibb])
    expected.append(sol_A)
    expected.append(sol_B)
    expected.append(sol_C)
    ### DONE FINDING EXPECTED OUTPUT ###

    # Remove the query strings
    for indexNum in range(len(queries)):
        test_output = test_output.replace(
            queries[letterList[indexNum]], '', 1).strip()

    # Check the result
    if test_output in expected:
        pass
    # If there was an error raised
    elif test_error != '':
        print(f'Your program outputted the following error:\n{test_error}')
        correct = False
        break
    else:
        correct = False

        # Shorten response output
        test_output = (
            test_output[:80] + (test_output[80:] and '..')).replace('\n', ' ')
        solution = []

        string_sol_A = str(sol_A)
        sol_A_short = (
            string_sol_A[:80] + (string_sol_A[80:] and '..')).replace('\n', ' ')
        solution.append(sol_A_short)

        string_sol_B = str(sol_B)
        sol_B_short = (
            string_sol_B[:80] + (string_sol_B[80:] and '..')).replace('\n', ' ')
        solution.append(sol_B_short)

        sol_C_short = (sol_C[:80] + (sol_C[80:] and '..')).replace('\n', ' ')
        solution.append(sol_C_short)

        # Tell user how it failed
        print(f'Input A: {inputA}')
        print(
            'Truncated to show first 80 characters, if present newlines replaced as spaces.')
        print(f'Outputted: {repr(test_output)}')
        print(f'Expected:  {repr(solution[0])}')
        print(f'Alt Ans.:  {repr(solution[1])}')
        print(f'Alt Ans.:  {repr(solution[2])}')
        break

if correct:
    print('Congrats!, you did it correctly.')
