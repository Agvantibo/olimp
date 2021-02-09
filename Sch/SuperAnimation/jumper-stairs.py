#!/bin/pypy3
from tkinter import *
from random import randint

root = Tk()
W, H = 800, 600
root.title("Geometry Dash Lite")
cnv = Canvas(root, width=W, height=H, bg="blue")
cnv.pack()

h = H // 2
w = W // 2

thingy = 50
o = cnv.create_rectangle(0, h - thingy, thingy, h, fill='yellow')

vx, vy = 2, 0
ambient_vx = 3
g = 0.3
jump = False

platforms_ground = []
platforms_wall_l = []

a1 = cnv.create_rectangle(0, H // 4 * 3, W // 3, H, fill="green")
platforms_ground.append([0, W // 3, H // 4 * 3])

a2 = cnv.create_rectangle(W // 3, H // 4 * 2, W // 3 * 2, H, fill="green")
platforms_ground.append([W // 3, W // 3 * 2, H // 4 * 2])
platforms_wall_l.append(W // 3)

a3 = cnv.create_rectangle(W // 3 * 2, H // 4, W, H, fill="green")
platforms_ground.append([W // 3 * 2, W, H // 4])
platforms_wall_l.append(W // 3 * 2)


def get_ground(x1, x2,  info, fallback):
    for i in info:
        if i[0] <= x1 <= i[1] or i[0] <= x2 <= i[1]:
            print(i[2])
            return i[2]
    return fallback


def is_jump_time(x2, info):
    for i in info:
        if i - 100 <= x2 <= i:
            print("Fired!")
            return True
    return False


def animate():
    global vy, jump, platforms_ground, platforms_wall_l

    cnv.move(o, vx, vy)

    x1, y1, x2, y2 = cnv.coords(o)

    if x1 > W:
        cnv.move(o, -(W + (W - x2)), 0)

    if y2 >= get_ground(x1, x2, platforms_ground, W):
        cnv.move(o, 0, get_ground(x1, x2, platforms_ground, W) - y2)

        if is_jump_time(x2, platforms_wall_l):
            vy -= 14
        else:
            vy -= 4
    else:
        vy += g

    cnv.after(10, animate)


animate()

mainloop()
