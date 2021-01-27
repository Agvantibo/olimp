#!/bin/python3
from tkinter import *
from random import *
from libcolor import *

s = 10
master = Tk()
# Window titlebar :)
master.title("Long Live Kali Linux")
W, H = s * 50, s * 50
cnv = Canvas(master, width=W, height=H, bg = "black")
cnv.pack()
fawkes = PhotoImage(file="./fawkes.png")

bg = color(fawkes.get(0, 0)[0], fawkes.get(0, 0)[1], fawkes.get(0, 0)[2])
for i in range(50):
    for j in range(50):
        cur = color(fawkes.get(i, j)[0], fawkes.get(i, j)[1], fawkes.get(i, j)[2])
        if bg.to_tuple() != cur.to_tuple():
            cnv.create_text(i*s, j*s, text=choice(["k", "a", "l", "i", "$"]), fill=cur.to_hex())

master.mainloop()
