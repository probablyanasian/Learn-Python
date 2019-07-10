#!/usr/bin/env python3
import os
import sys
import secrets
import string
from subprocess import Popen, PIPE, STDOUT

path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'2-practice.py')

while True:
  check_type = input("How many letters: ")
  if check_type.isdigit():
    if int(check_type) <= 2:
      print('Make it least greater than two.')
    else:
      break
  else:
    print('Input was not a number')
num_of_let = int(check_type)

while True:
  check_type = input("Front or back: ").lower()
  if check_type in ['front', 'back', 'f', 'b']:
    break
  else:
    print('Input has to be either \'front\' or \'back\'')

p = Popen([sys.executable, '-u', path], stdout=PIPE, stdin=PIPE, stderr=PIPE, encoding='utf-8')

#Get the query string
query = p.communicate()[0]
p.wait()

def text_gen(letters):
  return (''.join(secrets.choice(string.ascii_letters) for _ in range(letters)))

if check_type in ['front', 'f']:
  start_num = num_of_let
  end_num = 20
  expected = 'start_text'

elif check_type in ['back', 'b']:
  start_num = 20
  end_num = num_of_let
  expected = 'ending_text'
else:
  print('Error, please report this `2-check.py broke`')
  sys.exit()

correct = True
for _ in range(10): 
  p = Popen([sys.executable, '-u', path], stdout=PIPE, stdin=PIPE, encoding='utf-8')
  start_text = text_gen(start_num)
  ending_text = text_gen(secrets.randbelow(end_num))
  input_text = start_text + ending_text
  check = p.communicate(input=input_text)[0].replace(query, '').strip()
  if check == eval(expected):
    pass
  else: 
    correct = False
    print(f'Input: {input_text}')
    print(f'Outputted: {check}')
    print(f'Expected: {eval(expected)}')
    break
  p.wait()

if correct:
  print("Congrats! Your answer was correct.")