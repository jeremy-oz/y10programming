#======================
# imports tools
#======================
import tkinter as tk
from tkinter import ttk

# Create object
win = tk.Tk()

# Add a title
win.title("Student Survey")

# Adding a Label that will get modified
tea_drinkers = 0
coffee_drinkers = 0
tea_label = ttk.Label(win, text=f"{tea_drinkers} students drinks tea")
tea_label.grid(row=0, column=0)

coffee_label = ttk.Label(win, text=f"{coffee_drinkers} students drinks tea")
coffee_label.grid(row=1, column=0)


def click_tea():
    global tea_drinkers
    tea_drinkers += 1
    tea_label.configure(text=f"{tea_drinkers} student drinks tea")


def click_coffee():
    global coffee_drinkers
    coffee_drinkers += 1
    coffee_label.configure(text=f"{coffee_drinkers} student drinks coffee")

# Adding a Button
drink_tea = ttk.Button(win, text="I drink Tea!", command=click_tea)
drink_tea.grid(row=0, column=1)

drink_coffee = ttk.Button(win, text="I drink Coffee!", command=click_coffee)
drink_coffee.grid(row=1, column=1)


#======================
# Start GUI
#======================
win.mainloop()
