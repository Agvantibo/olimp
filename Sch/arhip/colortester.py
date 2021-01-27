#!/bin/python3
from tkinter import*
from random import*
from math import*

master=Tk()
w=800; h=500
cnv = Canvas(master, width = w, height = h)
cnv.pack()
img=PhotoImage(file='arhip.png')
cnv.create_image(0,0,anchor=NW, image=img)


def digit(x):
    if x <= 9:
        return str(x)
    elif x == 10:
        return 'a'
    elif x == 11:
        return 'b'
    elif x == 12:
        return 'c'
    elif x == 13:
        return 'd'
    elif x == 14:
        return 'e'
    elif x == 15:
        return 'f'


def real_color(r, g, b):
    minimal = min([r, g, b])
    return r - minimal, g - minimal, b - minimal


def code(x):
    a = x // 16
    b = x % 16
    return digit(a) + digit(b)

def color_code(r, g, b):
    return '#'+code(r)+code(g)+code(b)

x, y = [int(i) for i in input("enter the coordinates").split()]
r, g, b = img.get(x, y)
rr, rg, rb = real_color(r, g, b)
hex = color_code(r, g, b)
real_hex = color_code(rr, rg, rb)

print(r, g, b, rr, rg, rb, hex, real_hex)

mainloop()
