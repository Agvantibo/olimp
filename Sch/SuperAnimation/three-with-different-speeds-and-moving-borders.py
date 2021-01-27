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
border_left = Cnv.create_line(rect_mid(1, H / 2, H - 1, 0), fill="white")
border_right = Cnv.create_line(rect_mid(W - 1, H / 2, H - 1, 0), fill="white")

vx_slow = 4
vx_mid = 5
vx_fast = -6
vx_border = 2


def animate():
    global vx_slow, vx_mid, vx_fast, vx_border

    x1s, y1s, x2s, y2s = Cnv.coords(slow)
    x1m, y1m, x2m, y2m = Cnv.coords(mid)
    x1f, y1f, x2f, y2f = Cnv.coords(fast)
    xlb, none, none, none = Cnv.coords(border_left)

    if x2s >= W or x1s <= 0:
        vx_slow = -vx_slow
    if x2m >= W or x1m <= 0:
        vx_mid = -vx_mid
    if x2f >= W or x1f <= 0:
        vx_fast = -vx_fast
    if xlb >= W // 3 or xlb <= 0:
        vx_border = -vx_border

    if x2f >= x1s >= x1f or x2f >= x2s >= x1s:
        vx_slow = -vx_slow
        vx_fast = -vx_fast
    if x2s >= x1m >= x1s or x2s >= x2m >= x1s:
        vx_slow = -vx_slow
        vx_mid = -vx_mid
    if x2f >= x1m >= x1f or x2f >= x2m >= x1f:
        vx_fast = -vx_fast
        vx_mid = -vx_mid

    if x1s <= xlb or x2s >= W - xlb:
        vx_slow = -vx_slow
        Cnv.move(slow, 6, 0)
    if x1m <= xlb or x2m >= W - xlb:
        vx_mid = -vx_mid
        Cnv.move(mid, 6, 0)
    if x1f <= xlb or x2f >= W - xlb:
        vx_fast = -vx_fast
        Cnv.move(fast, 6, 0)

    Cnv.move(slow, vx_slow, 0)
    Cnv.move(mid, vx_mid, 0)
    Cnv.move(fast, vx_fast, 0)
    Cnv.move(border_left, vx_border, 0)
    Cnv.move(border_right, -vx_border, 0)

    Cnv.after(10, animate)


animate()

mainloop()
