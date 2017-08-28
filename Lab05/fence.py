from tkinter import *


tk = Tk()
c = Canvas(tk, width=400, height=400)
c.pack()

background = PhotoImage(file="grass.png")
c.image(200, 200, background)

tk.mainloop()
