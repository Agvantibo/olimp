#!/bin/python3
from tkinter import*
from random import randint

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
    return r - minimal, g - minimal, b - minimal, minimal


def code(x):
    a = x // 16
    b = x % 16
    return digit(a) + digit(b)

def color_code(r, g, b):
    return '#'+code(r)+code(g)+code(b)


def rect_mid(x, y, h, w):
    return (x - w // 2, y - h // 2, x + w // 2, y + h // 2)


for i in range(30000):
    x=randint(0, w -1)
    y=randint(0, h - 1)
    r,g,b=img.get(x,y)
    color=color_code(r, g, b)
    R = randint(2, 7)
    r, g, b, light = real_color(r, g, b)
    if g > 70 and b < 60:
        cnv.create_rectangle(rect_mid(x, y, randint(12, 16), randint(3, 7)),fill = color, outline=color)
    elif y > 440 and b > 20:
        cnv.create_oval(x-R,y-R,x+R*4,y+R/2,fill = color, outline=color)
    elif light > 70:
        cnv.create_oval(x-R,y-R,x+R,y+R,fill = color, outline=color)
    elif b > 130:
        cnv.create_rectangle(rect_mid(x, y, randint(3, 7), randint(12, 16)), fill = color, outline=color)
    else:
        cnv.create_oval(x-R,y-R,x+R,y+R,fill = color, outline=color)

mainloop()
