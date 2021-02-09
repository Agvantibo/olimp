#!/bin/pypy3
from tkinter import *

root = Tk()
W, H = 800, 600
cnv = Canvas(root, width=W, height=H)
root.title("Geometry Dash Lite Lite")
cnv.pack()

h = H // 2
w = W // 2

cnv.create_rectangle(0, 0, W, h, fill='blue', outline='')
cnv.create_rectangle(0, h, W, H, fill='green', outline='')
cnv.create_rectangle(w - 40,  h - 40, w, h, fill="red")
cnv.create_line(0, h, W, h)

a = 50
jumper = cnv.create_rectangle(0, h - a, a, h, fill='yellow')

vx, vy = 2, 0
g = 0.1


def animate():
    global vy, vx, w, h

    cnv.move(jumper, vx, vy)

    x1, y1, x2, y2 = cnv.coords(jumper)

    if x1 > W:
        cnv.move(jumper, -W - a, 0)

    if w - 70 < x2 < w:
        vy = -3

    if y2 < h:
        vy += g

    if y2 >= h:
        cnv.move(jumper, 0, h - y2)

    cnv.after(10, animate)


animate()

mainloop()
