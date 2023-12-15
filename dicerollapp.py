#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 15:01:16 2023

@author: hschrak
"""

import tkinter as tk
from tkinter import ttk
import random

def roll_dice(sides=6):
    return random.randint(1, sides)

def roll_and_display(event=None):
    try:
        sides = int(sides_spinbox.get())
        result.set(roll_dice(sides))
    except ValueError:
        result.set("Please enter a valid integer for sides.")


# Create the main window
app = tk.Tk()
app.title("Dice Roller")

# Create and configure widgets
sides_label = ttk.Label(app, text="Number of Sides:")
sides_spinbox = ttk.Spinbox(app, from_=1, to=100, value=6)
roll_button = ttk.Button(app, text="Roll Dice", command=roll_and_display)
result_label = ttk.Label(app, text="Result: ")
result = tk.StringVar()
result_display = ttk.Label(app, textvariable=result)

# Arrange widgets in a grid
sides_label.grid(row=0, column=0, padx=5, pady=5)
sides_spinbox.grid(row=0, column=1, padx=5, pady=5)
roll_button.grid(row=1, column=0, columnspan=2, pady=10)
result_label.grid(row=2, column=0, padx=5, pady=5)
result_display.grid(row=2, column=1, padx=5, pady=5)

sides_spinbox.bind('<Return>', roll_and_display)
roll_button.bind('<Return>', roll_and_display)
roll_button.focus_set()
sides_spinbox.focus_set()
# Start the Tkinter event loop
app.mainloop()
