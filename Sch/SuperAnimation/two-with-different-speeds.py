#!/bin/python3
from libcolor import Color
from tkinter import Tk, Canvas, mainloop
from animagick import rect_mid

# set window
root = Tk()
H, W = 900, 900
Cnv = Canvas(width=W, height=H, bg="black")
root.title("Jumpy Squares")
Cnv.pack()

# Draw initial stuff
color_slow = Color(106, 255, 0)     # green
color_fast = Color(255, 0, 0)       # red
slow = Cnv.create_rectangle(rect_mid(W / 2 + 90, H / 2, 50, 50), fill=color_slow.to_hex())
fast = Cnv.create_rectangle(rect_mid(W / 2 - 90, H / 2, 50, 50), fill=color_fast.to_hex())

vx_slow = 2
vx_fast = -4


def animate():
    global vx_slow, vx_fast

    x1s, y1s, x2s, y2s = Cnv.coords(slow)
    x1f, y1f, x2f, y2f = Cnv.coords(fast)

    if x2s > W or x1s < 0:
        vx_slow = -vx_slow

    if x2f > W or x1f < 0:
        vx_fast = -vx_fast

    if x2f >= x1s >= x1f or x2f >= x2s >= x1s:
        vx_slow = -vx_slow
        vx_fast = -vx_fast

    Cnv.move(slow, vx_slow, 0)
    Cnv.move(fast, vx_fast, 0)

    Cnv.after(10, animate)


animate()

mainloop()
