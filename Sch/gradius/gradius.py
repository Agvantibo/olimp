#!/bin/python3

from tkinter import *
from libcolor import *
from random import *

master = Tk()
W, H = 1000, 1000
cnv = Canvas(master, width=W, height=H)
cnv.pack()

init = color(255, 0, 0)
stop = color(0, 30, 255)
cur = color(0, 0, 0)

for i in range(50000):
    x = randint(0, H - 1)
    y = randint(0, H - 1)
    cur.r = int(init.r - y * (init.r - stop.r) / (H - 1))
    cur.g = int(init.g - y * (init.g - stop.g) / (H - 1))
    cur.b = int(init.b + y * (stop.b - init.b) / (H - 1))
    cnv.create_oval(rect_mid(x, y, 100, 100), fill=cur.to_hex(), outline=cur.to_hex())
    cnv.create_line(0, y, H, y, fill=cur.to_hex())

# init = color(255, 170, 0)
# stop = color(100, 255, 0)
# cur = color(0, 0, 0)

# for y in range(2*H):
#    cur.r=int(init.r+y*(stop.r-init.r)/(2*H-1))
#    cur.g=int(init.g+y*(stop.g-init.g)/(2*H-1))
#    cur.b=int(init.b+y*(stop.b-init.b)/(2*H-1))
#    x1=0
#    y1=y
#    x2=y
#    y2=0
#    cnv.create_line(0,y,H,y-H,fill=cur.to_hex())

mainloop()
