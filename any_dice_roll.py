#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:29:25 2023

@author: hschrak
"""

import random

def roll_dice(sides, num_rolls):
    results = []
    for _ in range(num_rolls):
        result = random.randint(1, sides)
        results.append(result)
    return results

# Get user input
sides = int(input("Enter the number of sides on the dice: "))
num_rolls = int(input("Enter the number of times to roll the dice: "))

# Roll the dice
dice_rolls = roll_dice(sides, num_rolls)

# Print the results
print("Results of rolling a", sides, "sided dice", num_rolls, "times:")
print(*dice_rolls)
