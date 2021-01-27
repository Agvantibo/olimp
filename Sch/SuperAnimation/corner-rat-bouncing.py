#!/bin/python3
from libcolor import Color
from tkinter import Tk, Canvas, mainloop

# set window
root = Tk()
H, W = 600, 600
Cnv = Canvas(width=W, height=H, bg="black", cursor="exchange")
root.title("Cornering Squares (with wall)")
Cnv.pack()

# Draw initial stuff
color_slow = Color(106, 255, 0)     # green
slow = Cnv.create_rectangle(0, 0, 100, 100, fill=color_slow.to_hex())
wall = Cnv.create_rectangle(W/2-4, 0, W/2+4, 100, fill="red")

vx_slow = -4
vy_slow = 0
direction = True


def animate():
    global vx_slow, vy_slow
    global direction

    x1s, y1s, x2s, y2s = Cnv.coords(slow)
    x1b, y1b, x2b, y2b = Cnv.coords(wall)

    if x1s <= x1b <= x2s and y1s <= 2:
        print('Bounced wall from right')
        Cnv.move(slow, x2s - x1b, 0)
        vx_slow = -vx_slow
        direction = not direction
    elif x1s <= x2b <= x2s and y1s <= 2:
        print('Bounced wall from left')
        Cnv.move(slow, x2s - x2b, 0)
        vx_slow = -vx_slow
        direction = not direction

    if direction:
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
    else:
        if x2s > W:
            vx_slow = 0
            vy_slow = 4
            Cnv.move(slow, W - x2s, 0)
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

    Cnv.move(slow, vx_slow, vy_slow)

    print(x1s, y1s, x2s, y2s)
    Cnv.after(10, animate)


animate()

mainloop()
