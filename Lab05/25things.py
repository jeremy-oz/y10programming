from tkinter import *
from random import choice, randint

gap = 10
lip_colors = ['red', 'tomato', 'salmon', 'firebrick1', 'indian red']
eye_color = ['blue', 'black', 'green', 'brown']

tk = Tk()
# decide the size and background colour of your canvas
c = Canvas(tk, width=600, height=600, bg='dim gray')
c.pack()


for i in range(5):
    for j in range(1):
        newx, newy = randint(0, 5), randint(0, 5)

        x11 = 20 + 100*i + gap*i + newx
        y11 = 20 + newy
        x12 = 40 + 100*i + gap*i + newx
        y12 = 40 + newy
        c.create_oval(x11, y11, x12, y12, fill=choice(eye_color))

        x21 = 20 + 50 + 100 * i + gap*i
        y21 = 20
        x22 = 40 + 50 + 100 * i + gap*i
        y22 = 40
        c.create_oval(x21, y21, x22, y22, fill=choice(eye_color))

        x31 = 10 + 100 * i + gap*i
        y31 = 10
        x32 = 100 + 100 * i + gap*i
        y32 = 100
        c.create_arc(x31, y31, x32, y32, extent=180, start=180, width=4, fill=choice(lip_colors), outline='pink')

tk.mainloop()