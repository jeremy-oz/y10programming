# add eyebrows

from tkinter import *


tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_oval(10, 10, 100, 100) # face
canvas.create_oval(30, 30, 45, 40) # left eye
canvas.create_oval(30+35, 30, 45+35, 40) # right eye

canvas.create_line(30-5, 25, 45+5, 25) # left eyebrow
canvas.create_line(30+35, 25, 45+5+35, 25) # right eyebrow
