#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:56:03 2023

@author: hschrak
"""

"""
Functions for simple reading to and writing from a file.

Author: Hunter Schrak
Date:   11-29-2023
"""


def count_lines(filepath):
    """
    Returns the number of lines in the given file.
    
    Lines are separated by the '\n' character, which is standard for Unix files.
    
    Parameter filepath: The file to be read
    Precondition: filepath is a string with the FULL PATH to a text file
    """
    # HINT: Remember, you can use a file in a for-loop
                # Implement me
    total = 0
    
    with open(filepath, 'r') as file:
        for line in file:
            total += 1
    
    return total


def write_numbers(filepath,n):
    """
    Writes the numbers 0..n-1 to a file.
    
    Each number is on a line by itself.  So the first line of the file is 0,
    the second line is 1, and so on. Lines are separated by the '\n' character, 
    which is standard for Unix files.  The last line (the one with the number
    n-1) should NOT end in '\n'
    
    Parameter filepath: The file to be written
    Precondition: filepath is a string with the FULL PATH to a text file
    
    Parameter n: The number of lines to write
    Precondition: n is an int > 0.
    """
    # HINT: You can only write strings to a file, so convert the numbers first
    
    with open(filepath, 'a') as file:
        for number in range(n):
            if number == n - 1:
                file.write(str(number))
            else:
                file.write(str(number) + '\n')
                
                
                
                
                """
Module with a function to read CSV files (converting them into a 2D list)

This function will be used in the main project.  You should hold on to it.

Author: Hunter Schrak
Date: 11-29-2023
"""
import csv


def read_csv(filename):
    """
    Returns the contents read from the CSV file filename.
    
    This function reads the contents of the file filename and returns the contents as
    a 2-dimensional list. Each element of the list is a row, with the first row being
    the header. Cells in each row are all interpreted as strings; it is up to the 
    programmer to interpret this data, since CSV files contain no type information.
    
    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file 
    is a valid CSV file
    """
    with open(filename, 'r') as file:
        csvFile = csv.reader(file)
        rows = list(csvFile)
    
    return rows


"""
Module with a function to write CSV files (using data in a 2D list)

This function will be used in the main project.  You should hold on to it.

Author: Hunter Schrak
Date: 11-29-2023
"""
import csv


def write_csv(data,filename):
    """
    Writes the given data out as a CSV file filename.
    
    To be a proper CSV file, data must be a 2-dimensional list with the first row 
    containing only strings.  All other rows may be any Python value.  Dates are
    converted using ISO formatting. All other objects are converted to their string
    representation.
    
    Parameter data: The Python value to encode as a CSV file
    Precondition: data is a  2-dimensional list
    
    Parameter filename: The file to read
    Precondition: filename is a string representing a path to a file with extension
    .csv or .CSV.  The file may or may not exist.
    """
    with open(filename, 'w', newline='') as csv_file:
        csvWriter = csv.writer(csv_file)

        # Write each row to the CSV file
        for row in data:
            csvWriter.writerow(row)


"""
Module with a functions to read and write JSON files (using dictionaries)

This function will be used in the main project.  You should hold on to it.

Author: Hunter Schrak
Date: 12-2-2023
"""
import json


def read_json(filename):
    """
    Returns the contents read from the JSON file filename.
    
    This function reads the contents of the file filename, and will use the json module
    to covert these contents into a Python data value.  This value will either be a
    a dictionary or a list. 
    
    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file 
    is a valid JSON file
    """
    with open(filename) as file:
        data = json.load(file)
        return data




def write_json(data,filename):
    """
    Writes the given data out as a JSON file filename.
    
    To be a proper JSON file, data must be a a JSON valid type.  That is, it must be
    one of the following:
        (1) a number
        (2) a boolean
        (3) a string
        (4) the value None
        (5) a list
        (6) a dictionary
    The contents of lists or dictionaries must be JSON valid type.
    
    When written, the JSON data should be nicely indented four spaces for readability.
    
    Parameter data: The Python value to encode as a JSON file
    Precondition: data is a JSON valid type
    
    Parameter filename: The file to read
    Precondition: filename is a string representing a path to a file with extension
    .json or .JSON.  The file may or may not exist.
    """
    with open(filename, "w") as outfile:
        j = json.dumps(data, indent=4)
        outfile.write(j)
        
 




"""
Functions for working with datetime objects.

Author: Hunter Schrak
Date:   12-2-2023
"""
import datetime


def christmas_day(year):
    """
    Returns ISO day of the week for Christmas in the given year.
    
    The ISO day is an integer between 1 and 7.  It is 1 for Monday, 7 for Sunday 
    and the appropriate number for any day in-between. 
    
    Parameter year: The year to check for Christmas
    Precondition: years is an int > 0 (and a year using the Gregorian calendar)
    """
    
    xMas = datetime.date(year,12,25)
    return xMas.isoweekday()




def iso_str(d,t):
    """
    Returns the ISO formatted string of date and time together.
    
    When combining, the time must be accurate to the microsecond.
    
    Parameter d: The month-day-year
    Precondition: d is a date object
    
    Parameter t: The time of day
    Precondition: t is a time object
    """
    # HINT: Combine date and time into a datetime and use isoformat
    result = datetime.datetime.combine(d, t)
    return result.isoformat()


"""
A simple function comparing datetime objects.

Author: Hunter Schrak
Date:   12-2-2023
"""
import datetime


def is_before(d1,d2):
    """
    Returns True if event d1 happens before d2.
    
    Values d1 and d2 can EITHER be date objects or datetime objects.
    If a date object, assume that it happens at midnight of that day. 
    
    Parameter d1: The first event
    Precondition: d1 is EITHER a date object or a datetime object
    
    Parameter d2: The first event
    Precondition: d2 is EITHER a date object or a datetime object
    """
    # HINT: Check the type of d1 or d2. If not a datetime, convert it for comparison
    if not isinstance(d1, datetime.datetime):
        d1 = datetime.datetime.combine(d1, datetime.time())
    
    if not isinstance(d2, datetime.datetime):
        d2 = datetime.datetime.combine(d2, datetime.time())
    
    return d1 < d2


import datetime


def past_a_week(d1,d2):
    """
    Returns True if event d2 happens at least a week (7 days) after d1.
    
    If d1 is after d2, or d2 is less than a week after d1, this function returns False.
    Values d1 and d2 can EITHER be date objects or datetime objects.  If a date object,
    assume that it happens at midnight of that day. 
    
    Parameter d1: The first event
    Precondition: d1 is EITHER a date object or a datetime object
    
    Parameter d2: The second event
    Precondition: d2 is EITHER a date object or a datetime object
    """
    # HINT: Check the type of d1 or d2. If not a datetime, convert it for comparison

    if not isinstance(d1, datetime.datetime):
        d1 = datetime.datetime.combine(d1, datetime.time())
    
    if not isinstance(d2, datetime.datetime):
        d2 = datetime.datetime.combine(d2, datetime.time())
    
    td = d2 - d1
    return td >= datetime.timedelta(days=7)


from dateutil.parser import parse

def str_to_time(timestamp):
    """
    Returns the datetime object for the given timestamp (or None if the stamp is invalid)
    
    This function should just use the parse function in dateutil.parser to convert the
    timestamp to a datetime object.  If it is not a valid date (so the parser crashes), 
    this function should return None.
    
    Parameter timestamp: The time stamp to convert
    Precondition: timestamp is a string
    """
    # Hint: Use a try-except to return None if parsing fails
    try:
        return parse(timestamp)
    except:
        return None



def sunset(date,daycycle):
    """
    Returns the sunset datetime (day and time) for the given date
    
    This function looks up the sunset from the given daycycle dictionary. If the
    daycycle dictionary is missing the necessary information, this function 
    returns the value None.
    
    A daycycle dictionary has keys for several years (as int).  The value for each year
    is also a dictionary, taking strings of the form 'mm-dd'.  The value for that key 
    is a THIRD dictionary, with two keys "sunrise" and "sunset".  The value for each of 
    those two keys is a string in 24-hour time format.
    
    For example, here is what part of a daycycle dictionary might look like:
        
        "2015": {
            "01-01": {
                "sunrise": "07:35",
                "sunset":  "16:44"
            },
            "01-02": {
                "sunrise": "07:36",
                "sunset":  "16:45"
            },
            ...
        }
    
    Parameter date: The date to check
    Precondition: date is a date object
    
    Parameter daycycle: The daycycle dictionary
    Precondition: daycycle is a valid daycycle dictionary, as described above
    """
    # HINT: ISO FORMAT IS 'yyyy-mm-ddThh:mm'.  Find the sunset value by constructing a
    # string in ISO format and calling str_to_time.
    
    year = date.year
    month_day = date.strftime("%m-%d")

    if str(year) in daycycle and month_day in daycycle[str(year)]:
        sunset_time_str = daycycle[str(year)][month_day].get("sunset")
        if sunset_time_str:
            timestamp_str = f"{year}-{month_day}T{daycycle[str(year)][month_day]['sunset']}"
            return str_to_time(timestamp_str)

    return None




from dateutil.parser import parse
import pytz
from datetime import tzinfo, datetime


def str_to_time(timestamp,tzsource=None):
    """
    Returns the datetime object for the given timestamp (or None if timestamp is 
    invalid).
    
    This function should just use the parse function in dateutil.parser to
    convert the timestamp to a datetime object.  If it is not a valid date (so
    the parser crashes), this function should return None.
    
    If the timestamp has a time zone, then it should keep that time zone even if
    the value for tzsource is not None.  Otherwise, if timestamp has no time zone 
    and tzsource is not None, then this function will use tzsource to assign 
    a time zone to the new datetime object.
    
    The value for tzsource can be None, a string, or a datetime object.  If it 
    is a string, it will be the name of a time zone, and it should localize the 
    timestamp.  If it is another datetime, then the datetime object created from 
    timestamp should get the same time zone as tzsource.
    
    Parameter timestamp: The time stamp to convert
    Precondition: timestamp is a string
    
    Parameter tzsource: The time zone to use (OPTIONAL)
    Precondition: tzsource is either None, a string naming a valid time zone,
    or a datetime object.
    """
    # HINT: Use the code from the previous exercise and add time zone handling.
    # Use localize if tzsource is a string; otherwise replace the time zone if not None
 
    try:
        parsed_time = parse(timestamp)
    except:
        return None

    if parsed_time.tzinfo is not None:
        return parsed_time

    if isinstance(tzsource, str):
        tz = pytz.timezone(tzsource)
        return tz.localize(parsed_time)
    elif isinstance(tzsource, tzinfo):
        return parsed_time.replace(tzinfo=tzsource)
    elif tzsource is None:
        return parsed_time
    elif isinstance(tzsource, datetime):
        return parsed_time.replace(tzinfo=tzsource.tzinfo)
    else:
        return None




def daytime(time,daycycle):
    """
    Returns True if the time takes place during the day, False otherwise (and 
    returns None if a key does not exist in the dictionary).
    
    A time is during the day if it is after sunrise but before sunset, as
    indicated by the daycycle dictionary.
    
    A daycycle dictionary has keys for several years (as strings).  The value for
    each year is also a dictionary, taking strings of the form 'mm-dd'.  The
    value for that key is a THIRD dictionary, with two keys "sunrise" and
    "sunset".  The value for each of those two keys is a string in 24-hour
    time format.
    
    For example, here is what part of a daycycle dictionary might look like:
    
        "2015": {
            "01-01": {
                "sunrise": "07:35",
                "sunset":  "16:44"
            },
            "01-02": {
                "sunrise": "07:36",
                "sunset":  "16:45"
            },
            ...
        }
    
    In addition, the daycycle dictionary has a key 'timezone' that expresses the
    timezone as a string. This function uses that timezone when constructing
    datetime objects using data from the daycycle dictionary.  Also, if the time
    parameter does not have a timezone, we assume that it is in the same timezone 
    as the daycycle dictionary.
    
    Parameter time: The time to check
    Precondition: time is a datetime object
    
    Parameter daycycle: The daycycle dictionary
    Precondition: daycycle is a valid daycycle dictionary, as described above
    """
    # HINT: Use the code from the previous exercise to get sunset AND sunrise
    # Add a timezone to time if one is missing (the one from the daycycle)
    year = str(time.year)
    month_day = time.strftime("%m-%d")

    if year in daycycle and month_day in daycycle[year]:
        sunrise_time_str = daycycle[year][month_day].get("sunrise")
        sunset_time_str = daycycle[year][month_day].get("sunset")

        if sunrise_time_str and sunset_time_str:
            sunrise = str_to_time(f"{year}-{month_day}T{sunrise_time_str}", daycycle["timezone"])
            sunset = str_to_time(f"{year}-{month_day}T{sunset_time_str}", daycycle["timezone"])

            if time.tzinfo is None:
                time = time.replace(tzinfo=sunrise.tzinfo)

            return sunrise < time < sunset

    return None
