#!/bin/python3
from tkinter import *
from libcolor import *
master = Tk()
W, H = 800, 700
cnv = Canvas(master, width=W, height=H)
cnv.pack()

cnv.create_line(0, 0, W - 1, H - 1, fill = input("Enter color hex: \n"))

mainloop()
