from tkinter import *
from tkinter import font
from random import randint
from time import sleep

tk = Tk()
c = Canvas(tk, width=800, height=600, bg='LemonChiffon2')
c.pack()

while True:
    x, y = randint(0, 800), randint(0, 600)
    rfont = font.Font(family='Times New Roman', size=randint(8, 48), weight='bold')
    rcolor = '#%6x' % randint(0x0, 0xFFFFFF)
    c.create_text(x, y, text='Jeremy Chen', font=rfont, fill=rcolor)
    tk.update()
    sleep(.2)
