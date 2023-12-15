#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:47:52 2023

@author: hschrak
"""

def percentIncrease(oldValue, newValue):
    """
    Calculates the percent increase between old_value and new_value.
    
    Returns:
    float: The percent increase.
    """
    percent_increase = ((newValue - oldValue) / abs(oldValue)) * 100
    return percent_increase

    
oldValue= float(input('Old Value: '))
newValue= float(input('New Value: '))
                  
result = percentIncrease(oldValue, newValue)

print(result)
    

