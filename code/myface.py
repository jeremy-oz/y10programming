from tkinter import *


tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

canvas.create_oval(10, 10, 100, 100)

tk.mainloop()
