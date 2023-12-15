#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 07:55:37 2023

@author: hschrak
"""

"""
Module that validates the flight school's records.

This is the primary module that does all of the work. It loads the files, loops through
the lessons, and searches for any takeoffs that violate insurance requirements.

Technically, we could have put many of these functions in __main__.py.  That is the
main module of this application anyway.  However, for testing purposes we want all
functions in modules and we only want script code in the file __main__.py

Author: Hunter Schrak
Date: 12-11-2023
"""
import utils
import tests
import os.path
import violations

# FILES TO AUDIT
# Sunrise and sunset
DAYCYCLE = 'daycycle.json'
# Hourly weather observations
WEATHER  = 'weather.json'
# The list of insurance-mandated minimums
MINIMUMS = 'minimums.csv'
# The list of all registered students in the flight school
STUDENTS = 'students.csv'
# The list of all take-offs (and landings)
LESSONS  = 'lessons.csv'

def discover_violations(directory,output):
    """
    Searches the dataset directory for any flight lessons the violation regulations.
    
    This function will call list_weather_violations() to get the list of weather violations.
    If list_endorsment_violations (optional) is completed, it will call that too, as
    well as list_inspection_violations.  It will concatenate all of these 2d lists
    into a single 2d list of violations (so a flight may be listed more than once for
    each of the three types of violations).
    
    If the parameter output is not None, it will create the CSV file with name output
    and write the 2d list of violations to this file.  This CSV file should have the
    following header:
    
        STUDENT,AIRPLANE,INSTRUCTOR,TAKEOFF,LANDING,FILED,AREA,REASON
    
    Regardless of whether output is None, this function will print out the number of
    violations, as follows:
    
        '23 violations found.'
    
    If no violations are found, it will say
    
        'No violations found.'
    
    Parameter directory: The directory of files to audit
    Precondition: directory is the name of a directory containing the files 'daycycle.json',
    'weather.json', 'minimums.csv', 'students.csv', 'teachers.csv', 'lessons.csv',
    'fleet.csv', and 'repairs.csv'.
    
    Parameter output: The CSV file to store the results
    Precondition: output is None or a string that is a valid file name
    """
    daycycle = utils.read_json(os.path.join(directory, DAYCYCLE))
    weather = utils.read_json(os.path.join(directory, WEATHER))
    minimums = utils.read_csv(os.path.join(directory, MINIMUMS))
    students = utils.read_csv(os.path.join(directory, STUDENTS))
    lessons = utils.read_csv(os.path.join(directory, LESSONS))


    weather_viol = []
    # List weather violations
    weather_viol = violations.list_weather_violations(directory)

    # Concatenate weather violations

    # Print the number of violations found
    if len(weather_viol) > 1:
        print(f"{len(weather_viol)} violations found.")
    elif len(weather_viol) == 1:
        print(f'{len(weather_viol)} violation found.')
    else:
        print('No violations found.')
        # Print or write the violations

    # Write violations to CSV file
    if output:
        utils.write_csv([['STUDENT', 'AIRPLANE', 'INSTRUCTOR', 'TAKEOFF', 'LANDING', 'FILED', 'AREA', 'REASON']] + weather_viol, output)
    # Print violations to the screen



def execute(args):
    """
    Executes the application or prints an error message if executed incorrectly.
    
    The arguments to the application (EXCLUDING the application name) are provided to
    the list args. This list should contain either 1 or 2 elements.  If there is one
    element, it should be the name of the data set folder or the value '--test'.  If
    there are two elements, the first should be the data set folder and the second
    should be the name of a CSV file (for output of the results).
    
    If the user calls this script incorrectly (with the wrong number of arguments), this
    function prints:
    
        Usage: python auditor dataset [output.csv]
    
    This function does not do much error checking beyond counting the number of arguments.
    
    Parameter args: The command line arguments for the application (minus the application name)
    Precondition: args is a list of strings
    """
    # Quit if wrong number of arguments
    if len(args) != 1 and len(args) != 2:
        print('Usage: python auditor dataset [output.csv]')
    elif '--test' in args and len(args) > 1:
        print('Usage: python auditor dataset [output.csv]')
    elif '--test' in args:
        tests.test_all()
    else:
        dataset = args[0]
        output_file = args[1] if len(args) == 2 else None

        # Run the main application logic
        discover_violations(dataset, output_file)

