#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 09:16:31 2023

@author: hschrak
"""

import string
import secrets



length = int(input('Input password length: '))

symbols = input('Include symbols? (y/n): ')
symbols = symbols.lower() == 'y'
uppercase = input('Include uppercase letters? (y/n): ')
uppercase = uppercase.lower() == 'y'

def contain_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
        
    return False
        
def contain_symbol(password: str) -> bool:
    for char in password:
        if char.string.punctuation:
            return True
        
    return False

def generate_password(length: int, symbols: bool, uppercase: bool)-> str:

    
    
    combination: str = string.ascii_lowercase + string.digits
    
    if symbols:
        combination += string.punctuation
        
    if uppercase:
        combination += string.ascii_uppercase
        
    combination_len = len(combination)
    new_password: str = ''
    
    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_len)]
        
    return new_password

if __name__ == '__main__':
    password = generate_password(length, symbols, uppercase)
    print(f'Generated Password: {password}')

    