import tkinter as tk
from tkinter import ttk


def percent(part, whole):
    return 100 * float(part)/float(whole)

# part = float(input('part: '))
# whole = float(input('whole: '))
              
# result = percent(part, whole)

# print(result)
        

def calc_and_display(event=None):
    try:
        part = int(percent_spinbox1.get())
        whole = int(percent_spinbox2.get())
        result.set(percent(part, whole))
    except ValueError:
        result.set("Please enter a valid integer.")






# Create the main window
app = tk.Tk()
app.title("Percent Calculator")

# Create and configure widgets
percent_label1 = ttk.Label(app, text="Part Value:")
percent_spinbox1 = ttk.Spinbox(app, from_=1, to=100, value=6)
percent_label2 = ttk.Label(app, text="Whole Value:")
percent_spinbox2 = ttk.Spinbox(app, from_=1, to=100, value=6)
calc_button = ttk.Button(app, text="Calculate", command=calc_and_display)
result_label = ttk.Label(app, text="Result: ")
result = tk.StringVar()
result_display = ttk.Label(app, textvariable=result)

# Arrange widgets in a grid
percent_label1.grid(row=0, column=0, padx=5, pady=5)
percent_label2.grid(row=1, column=0, padx=5, pady=5)
percent_spinbox1.grid(row=0, column=1, padx=5, pady=5)
percent_spinbox2.grid(row=1, column=1, padx=5, pady=5)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)
result_label.grid(row=3, column=0, padx=5, pady=5)
result_display.grid(row=3, column=1, padx=5, pady=5)

percent_spinbox1.bind('<Return>', calc_and_display)
percent_spinbox2.bind('<Return>', calc_and_display)
calc_button.bind('<Return>', calc_and_display)
calc_button.focus_set()
percent_spinbox1.focus_set()
# Start the Tkinter event loop
app.mainloop()