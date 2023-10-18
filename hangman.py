#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 14:38:16 2023

@author: hschrak
"""

from random import choice

def run_game():
    word: str = choice(["dog", "cat", "car", "sun", "moon", "house", "chair", "apple", "dance", "music",
                        "smile", "river", "guitar", "flower", "ocean", "school", "laptop", "jungle", "forest", "family",
                        "friend", "purple", "orange", "butterfly", "morning", "evening", "rainbow", "elephant", "penguin", "giraffe",
                        "dolphin", "sandwich", "bicycle", "chocolate", "adventure", "beautiful", "happiness", "treasure", "mountain", "waterfall",
                        "cathedral", "vacation", "celebrate", "discovery", "imagination", "meditation", "experience", "happiness", "friendship", "happiness"])

    username: str = input('What is your name? ')
    print(f'Welcome to Hangman {username}.')

    guessed: str = ''
    tries: int = 6
    while tries > 0:
        blanks: int = 0

        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1

        print()  # adds a blank line

        if blanks == 0:
            print('That is correct!! Good job!!')
            break

        guess: str = input('Enter a letter: ')
        
        if guess == word:
            print(f'WOW, guessed {word} arent you a smarty pants!!')
            break
        
        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single letter.')
            continue


        if guess in guessed:
            print(f'You already used "{guess}". Please try another letter.')
        else:
            guessed += guess

        if guess not in word:
            tries -= 1
            print(f'Sorry, that is incorrect. You have {tries} tries remaining.')

        if tries == 0:
            print(f'The answer was {word}. YOU GET NOTHING!!...YOU LOSE!!...GOOD DAY SIR!!')
            break

if __name__ == '__main__':
    run_game()
