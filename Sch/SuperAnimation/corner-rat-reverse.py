#!/bin/python3
from libcolor import Color
from tkinter import Tk, Canvas, mainloop

# set window
root = Tk()
H, W = 600, 600
Cnv = Canvas(width=W, height=H, bg="black")
root.title("Cornering Squares (reverse)")
Cnv.pack()

# Draw initial stuff
color_slow = Color(106, 255, 0)     # green
slow = Cnv.create_rectangle(W - 100, 0, W, 100, fill=color_slow.to_hex())

vx_slow = -4
vy_slow = 0


def animate():
    global vx_slow, vy_slow

    Cnv.move(slow, vx_slow, vy_slow)

    x1s, y1s, x2s, y2s = Cnv.coords(slow)
    if y1s < 0:
        print("upper right")
        vx_slow = -4
        vy_slow = 0
        Cnv.move(slow, 0, -y1s)
    if x1s < 0:
        print('upper left')
        Cnv.move(slow, -x1s, 0)
        vx_slow = 0
        vy_slow = 4
    if y2s > H:
        print('lower left')
        Cnv.move(slow, 0, H - y2s)
        vx_slow = 4
        vy_slow = 0
    if x2s > W:
        print('lower right')
        Cnv.move(slow, W - x2s, 0)
        vx_slow = 0
        vy_slow = -4
    print(x1s, y1s, x2s, y2s)
    Cnv.after(10, animate)


animate()

mainloop()
