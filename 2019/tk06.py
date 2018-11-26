# a whole face with two colorful eyes

from tkinter import *


tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_oval(10, 10, 100, 100) # face
canvas.create_oval(30, 30, 45, 40, fill='blue') # left blue eye
canvas.create_oval(30+35, 30, 45+35, 40, fill='hot pink') # right blue eye

canvas.create_line(30-5, 25, 45+5, 25) # left eyebrow
canvas.create_line(30+35, 25, 45+5+35, 25) # right eyebrow

# draw a nose

canvas.create_rectangle(50, 45, 60, 70)

# add a mouth

# draw arc: two styles
# style 2: style=ARC, an arc line
canvas.create_arc(30, 50, 80, 90, extent=-180, style=ARC)
