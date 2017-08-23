from tkinter import *
from random import choice

colors = ['blue', 'green', 'red']

tk = Tk()
c = Canvas(tk, width=400, height=400)

x1 = 5
y1 = 5
x2 = x1 + 195
y2 = y1 + 195

c.create_oval(x1, y1, x2, y2, fill=choice(colors))
c.create_line(x1+50, y1+145, x2-45, y2-50)

x1 = 150
y1 = 150
x2 = x1 + 195
y2 = y1 + 195
c.create_oval(x1, y1, x2, y2, fill=choice(colors))
c.create_line(x1+50, y1+145, x2-45, y2-50)

c.pack()

tk.mainloop()
