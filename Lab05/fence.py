from tkinter import *

tk = Tk()
image_bg = PhotoImage(file="grass.gif")
# picture converted from: openclipart.org
# url: https://openclipart.org/download/168711/1330899616.svg

c = Canvas(tk, width=image_bg.width(), height=image_bg.height())
c.pack()


c.create_image(image_bg.width()/2, image_bg.height()/2, image=image_bg)

tk.mainloop()
