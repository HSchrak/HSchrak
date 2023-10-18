#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 11:53:44 2023

@author: hschrak5
"""

from random import randint

lower_num, higher_num = 1, 10
random_num: int = randint(lower_num, higher_num)
print(f'Guess an number between {lower_num} and {higher_num}. ')

max_guesses = 3

guess_count = 0

for guess_count in range (max_guesses):
    try:
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        print('Please enter a valid number.')
        continue
    if user_guess > random_num:
        print('The number is lower.')
    elif user_guess < random_num:
        print('The number is higher.')
    else: 
        print('you guessed it!')
        break
    
    guess_count += 1
    
if guess_count == max_guesses:
    print(f'Sorry, you ran out of guesses. The number was {random_num}.')