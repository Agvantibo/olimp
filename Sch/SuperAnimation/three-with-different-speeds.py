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
color_mid = Color(0, 221, 255)      # blue
color_fast = Color(255, 0, 0)       # red
slow = Cnv.create_rectangle(rect_mid(W / 2 + 90, H / 2, 40, 40), fill=color_slow.to_hex())
mid = Cnv.create_rectangle(rect_mid(W / 2, H / 2, 40, 40), fill=color_mid.to_hex())
fast = Cnv.create_rectangle(rect_mid(W / 2 - 90, H / 2, 40, 40), fill=color_fast.to_hex())

vx_slow = 2
vx_mid = 4
vx_fast = -6


def animate():
    global vx_slow, vx_mid, vx_fast

    x1s, y1s, x2s, y2s = Cnv.coords(slow)
    x1m, y1m, x2m, y2m = Cnv.coords(mid)
    x1f, y1f, x2f, y2f = Cnv.coords(fast)

    if x2s > W or x1s < 0:
        vx_slow = -vx_slow

    if x2m > W or x1m < 0:
        vx_mid = -vx_mid

    if x2f > W or x1f < 0:
        vx_fast = -vx_fast

    if x2f >= x1s >= x1f or x2f >= x2s >= x1s:
        vx_slow = -vx_slow
        vx_fast = -vx_fast
    if x2s >= x1m >= x1s or x2s >= x2m >= x1s:
        vx_slow = -vx_slow
        vx_mid = -vx_mid
    if x2f >= x1m >= x1f or x2f >= x2m >= x1f:
        vx_fast = -vx_fast
        vx_mid = -vx_mid

    Cnv.move(slow, vx_slow, 0)
    Cnv.move(mid, vx_mid, 0)
    Cnv.move(fast, vx_fast, 0)

    Cnv.after(10, animate)


animate()

mainloop()
