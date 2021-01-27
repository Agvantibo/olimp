#!/bin/python3
from libcolor import Color
from tkinter import Tk, Canvas, mainloop

# set window
root = Tk()
H, W = 600, 600
Cnv = Canvas(width=W, height=H, bg="black", cursor="exchange")
root.title("Cornering Squares")
Cnv.pack()

# Draw initial stuff
color_slow = Color(106, 255, 0)     # green
slow = Cnv.create_rectangle(0, 0, 100, 100, fill=color_slow.to_hex())

vx_slow = 4
vy_slow = 0


def animate():
    global vx_slow, vy_slow

    Cnv.move(slow, vx_slow, vy_slow)

    x1s, y1s, x2s, y2s = Cnv.coords(slow)

    if x2s > W:
        print("press f to pay respects")
        vx_slow = 0
        vy_slow = 4
        Cnv.move(slow, W-x2s, 0)
    elif y2s > H:
        Cnv.move(slow, 0, H - y2s)
        vx_slow = -4
        vy_slow = 0
    elif x1s < 0:
        Cnv.move(slow, -x1s, 0)
        vx_slow = 0
        vy_slow = -4
    elif y1s < 0:
        Cnv.move(slow, 0, -y1s)
        vx_slow = 4
        vy_slow = 0

    Cnv.after(10, animate)


animate()

mainloop()
