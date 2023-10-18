#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 13:26:56 2023

@author: hschrak
"""



def average(num_list):

    count = len(num_list)
    print(f'length of list: {count}')
    total = float(sum(num_list))
    print(f'Sum of numbers in list: {total}')
    avg = total / count 
    print(f'The average is {avg}')
        
    #return avg 
num_str = input('Enter a list of numbers: ')
num_str = num_str.strip('[]')
num_list = [float(num) for num in num_str.split(',')]
average(num_list)