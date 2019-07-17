#!/usr/bin/env python3
import os
import sys
import secrets
import string
from subprocess import Popen, PIPE, STDOUT

# Get the path this file is in
path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '4-practice.py')

# Make dict for query strings
queries = {}
queryNum = 0
# This time, 2 letters
for letter in list(string.ascii_uppercase)[:2]:
    # Open the process
    p = Popen([sys.executable, '-u', path],
              stdout=PIPE, stdin=PIPE, stderr=PIPE, encoding='utf-8')
    blank_input = '\04'
    if queryNum != 0:
        blank_input = '\n'+'\04'
    # Get the query string
    queries['query'+letter] = p.communicate(input=blank_input)[0]
    # Make sure the process closes
    queryNum += 1
    p.wait()

print(queries)

# correct = True
# for _ in range(25):
#     # Open another subprocess of it
#     p = Popen([sys.executable, '-u', path],
#               stdout=PIPE, stdin=PIPE, encoding='utf-8')
#     if True:
#         break
#     else:
#         # Not correct Exit the loop
#         correct = False
#         # Tell user how it failed
#         print(f'Input: {test_input}')
#         print(f'Outputted: {test_output}')
#         print(f'Expected: {expected_output}')
#         break
#     # Just in case it didn't close for some reason
#     p.wait()

# # If it was right
# if correct:
#     print("Congrats! Your answer was correct.")
