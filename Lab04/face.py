from tkinter import *
from time import sleep

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
#canvas.create_oval(200, 200, 200+150, 200+100)
#canvas.create_oval(200+30, 200+50, 200+55, 200+65)
#canvas.create_rectangle(20, 20, 120, 60)

x1, y1 = 50, 50
x2, y2 = x1+150, y1+200
canvas.create_line(x1, y1, x1+150, y1+200)
canvas.create_line(x1+150, y1+200, x1-150, y1+200)
canvas.create_line(x1-150, y1+200, x1, y1)
canvas.pack()

for i in range(100):
    canvas.move('all', 5, 5)
    tk.update()
    sleep(.1)

tk.mainloop()
