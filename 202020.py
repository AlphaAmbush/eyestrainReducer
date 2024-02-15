import sys
import time
from tkinter import *
import os


def countdown(count, label, master):
    label['text'] = count
    if count > 0:
        master.after(1000, countdown, count-1, label, master)


def EyeCareApp(master):

    flag_var = True
    master.title('Eye Care')

    def setFlag():
        sys.exit()

    canvas = Canvas(master, width=400, height=600, bg='orange')
    canvas.pack()

    label = Label(master, font=('Times 45'), bg='white')
    label.place(x=200, y=300)

    label2 = Label(master, font=('Times 20'),
                   text="LOOK AWAY!!!", bg='firebrick2')
    label2.place(x=130, y=380)

    label3 = Label(master, font=('Times 15'), bg='orange',
                   text="This app will help you \n relax your eyes after 20 min for 20 sec")
    label3.place(x=5, y=10)

    B = Button(master, text="Close the process",
               command=lambda: setFlag(), font=('Times 15'), bg='lightblue')
    B.pack()

    countdown(20, label, master)
    return flag_var


flag = True

while flag:
    root = Tk()
    flag = EyeCareApp(root)
    root.after(20000, lambda: root.destroy())
    root.mainloop()
    time.sleep(1200)
