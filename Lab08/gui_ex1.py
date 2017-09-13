from tkinter import *

def main():
    root = Tk()
    root.title('Student Survey')
    label = Label(root, text='Do you prefer tea or coffee?')
    button1 = Button(root, text='Tea')
    button2 = Button(root, text='Coffee')
    label.pack()
    button1.pack()
    button2.pack()
    root.mainloop()

if __name__ == '__main__':
    main()
