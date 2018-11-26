# Draw a circle like object using oval
# oval = canvas.create_oval(x0, y0, x1, y1, options)

from tkinter import *


tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_oval(10, 10, 100, 100)
