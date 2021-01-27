#!/bin/python3
from tkinter import *
from random import *
from libcolor import *

s = 10
master = Tk()
# Window title-bar :)
master.title("Change_me")
s = 15
h = s*50
w = s*50
cnv = Canvas(master, height=h, width=w)
background = "black"
cnv = Canvas(master, width=h, height=w, bg=background)
cnv.pack()
r1, g1, b1 = img.get(0,0)
files = []
for i in range(48):
    files.append(PhotoImage(file="./frames/frame_" + str(i) + ".png"))
for f in files:
    for i in range(50):
        for j in range(50):
            r,g,b = f.get(i,j)
            if (r,g,b)!=(r1,g1,b1):
                symbols = ['m', "a", 'r', "i", "o"]
                t = symbols[randint(0,len(symbols)-1)]
                cnv.create_text(i*s,j*s, text = t, fill = color_code(r,g,b), font = ('Engravers MT', s))


animate()
master.mainloop()
