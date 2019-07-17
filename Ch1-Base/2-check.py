#!/usr/bin/env python3
import os
import sys
import secrets
import string
from subprocess import Popen, PIPE, STDOUT

# Get the path this file is in
path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '2-practice.py')

# Get the amount of letters to check for
while True:
    num_of_let = input("How many letters: ")
    if num_of_let.isdigit():
        num_of_let = int(num_of_let)
        if num_of_let <= 2:
            print('Make it least greater than two.')
        else:
            break
    else:
        print('Input was not a number')

# Get whether to check in the front or in the back
while True:
    check_type = input("Front or back: ").lower()
    if check_type in ['front', 'back', 'f', 'b']:
        if check_type in ['front', 'f']:
            start_num = num_of_let
            end_num = 20
            expected = 'start_text'

        elif check_type in ['back', 'b']:
            start_num = 20
            end_num = num_of_let
            expected = 'ending_text'
        break
    else:
        print('Input has to be either \'front\' or \'back\'')

# Open the process
p = Popen([sys.executable, '-u', path],
          stdout=PIPE, stdin=PIPE, stderr=PIPE, encoding='utf-8')

# Get the query string
query = p.communicate()[0]
# Make sure the process closes
p.wait()

# Random "word" generator


def text_gen(letters):
    return (''.join(secrets.choice(string.ascii_letters) for _ in range(letters)))


correct = True
for _ in range(25):
    # Open another subprocess of it
    p = Popen([sys.executable, '-u', path],
              stdout=PIPE, stdin=PIPE, encoding='utf-8')
    # Set the desired length of texts
    start_text = text_gen(start_num)
    ending_text = text_gen(end_num)
    # put the two together
    input_text = f'{start_text}{ending_text}'
    # Send in the text, get rid of the query text
    check = p.communicate(input=input_text)[0].replace(query, '', 1)
    # Check if the response was right
    if check == eval(expected):
        # Do nothing
        pass
    else:
        # Not correct Exit the loop
        correct = False
        # Tell user how it failed
        print(f'Input: {input_text}')
        print(f'Outputted: {check}')
        print(f'Expected: {eval(expected)}')
        break
    # Just in case it didn't close for some reason
    p.wait()

# If it was right
if correct:
    print("Congrats! Your answer was correct.")
