#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 13:16:06 2023

@author: hschrak
"""

import sys

print("Welcome to my mythology trivia game.")

playing = input('Do you want to play? ')

if playing.lower() not in {'yes', 'sure', 'why not', 'i guess', 'mos def', 'yeah', 'yerp', 'yea', 'yup'}:
    print ('whatever, i didnt want to hang with you anyway') 
    sys.exit()
        
else: print('HELL YEAH LETS PLAY!') 
score = 0
print('Remember SPELLING MATTERS!!!')
    
print('Question 1')
answer = input('Who flew to close to the sun? ') 
if answer.lower() == "icarus":
    print('Correct!')
    score += 1
else: print('Incorrect')

print('Question 2')
answer = input('Greek god of the sea is Posidon, who is the Roman god of the sea? ') 
if answer.lower() == "neptune":
    print('Correct!')
    score += 1
else: print('Incorrect')

print('Question 3')
answer = input("Zeus' demi-god son? ") 
if answer.lower() == "hercules" or answer.lower() == "heracles":
    print('Correct!')
    score += 1
else: print('Incorrect')

print('Question 4')
answer = input('What creature had the body of a lion, wings of an eagle, and the head of a woman? ') 
if answer.lower() == "sphinx":
    print('Correct!')
    score += 1
else: print('Incorrect')

print('Question 5')
answer = input('Prometheus is having his guts eaten for eternity for what crime against the gods? ') 
if answer.lower() == "stealing fire" or answer.lower() == "stole fire" or answer.lower() == "stolen fire":
    print('Correct!')
    score += 1
else: print('Incorrect')

print('Question 6, these questions will be Norse mythology based.')
answer = input('Yggdrasil, the ash tree that connects the nine realms also goes by this name? ') 
if answer.lower() == "the world tree" or answer.lower() == "world tree":
    print('Correct!')
    score += 1
else: print('Incorrect')

print('Question 7')
answer = input('What is the Norse apocolypse? ') 
if answer.lower() == "ragnarok":
    print('Correct!')
    score += 1
else: print('Incorrect')

print('Question 8')
answer = input('What is the name of the great wolf destined to devour the sun during Ragnarök? ') 
if answer.lower() == "fenrir":
    print('Correct!')
    score += 1
else: print('Incorrect')

print('Question 9')
answer = input('What is the name of the rainbow bridge that connects Asgard and Midgard? ') 
if answer.lower() == "bifrost":
    print('Correct!')
    score += 1
else: print('Incorrect')

print('Question 10, last one!')
answer = input('What is the name of the giant serpent that encircles the world? ') 
if answer.lower() == "jormungandr" or answer.lower() == "the world serpent" or answer.lower() == "the midgard serpent" or answer.lower() == "world serpent" or answer.lower() == "midgard serpent":
    print('Correct!')
    score += 1
else: print('Incorrect')

print('You got ' + str(score) + ' out of 10 questions correct.')
if score  == 5: 
    print('.500 is good if your playing baseball.')
if 2 < score  < 5 : 
    print('You know you could have just googled the answers?')
if 5 < score < 10 : 
    print('very well done you know your stuff!')
if score  == 10 :
    print('Perfect score! no notes.')
if score <= 2 :
    print('yikes...maybe you shouldnt have played.')









