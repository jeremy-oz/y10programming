from tkinter import *

tk = Tk()
c = Canvas(tk, width=800, height=600, bg='pale green')
c.pack()


for i in range(5):
    x = 35 * i
    y = 0
    # draw a paling
    c.create_polygon(20+x, 100+y, 20+x, 20+y, 30+x, 10+y, 40+x, 20+y, 40+x, 100+y, fill='sienna4')

tk.mainloop()
