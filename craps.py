#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 07:38:37 2023

@author: hschrak
"""

from random import randint
import sys

bank = 250  

def roll_two_dice():
    die1 = randint(1, 6)
    #print(f'first die: {die1}')
    die2 = randint(1, 6)
    #print(f'Second die: {die2}')
    return die1 + die2


def craps():
    global bank
    mark = roll_two_dice()
    print(f'Mark set: {mark}')


    while True:
        bet = int(input('Place your bet (enter 0 to exit): '))
        
        if bet == 0:
            print(f'your winnings: {bank}')
            sys.exit()
        
        print(f'Mark: {mark}')
        roll = roll_two_dice() 
        print(f'Roll result: {roll}')
        
        if roll == mark:
            bank += bet*2
            print(f'YOU HIT THE MARK!! Your winnings: {bet*2}. Your bank: {bank}')
        elif mark == 7 and roll!= mark:
            bank -= bet
            print(f'Your crapped out. your bank: {bank}')
            sys.exit()
        elif mark != 7 and roll==7:
            bank -= bet
            print(f'You crapped out. your bank: {bank}')
            sys.exit()
        else:
            bank += bet*.5
            print(f'YOU WON!! Your winnings: {bet*.5}. Your bank: {bank}')
            continue
        
        
if __name__=='__main__':
    craps() 