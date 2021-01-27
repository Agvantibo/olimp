#!/bin/python3
from tkinter import Tk, Canvas, mainloop
from libcolor import rainbow, rect_mid
master = Tk()
master.resizable(False, False)
W, H = [int(i) for i in input("Введите разрешение монитора в формате \"X Y\" \n").split()]
user = input("Должно ли окно иметь заголовок? (Д/н) Без заголовка его нельзя закрыть нормально!\n").lower()
if user == "н":
    master.overrideredirect(True)
cnv = Canvas(master, width=W, height=H, bg="black")
cnv.pack()


x, y, a = W/2, H/2, W/4
o = cnv.create_rectangle(rect_mid(x, y, a, a), fill='black')

vx = 2
vy = 3

rgb = []

for i in rainbow():
    rgb.append(i)

counter = 0


def animate():
    global vx, vy, counter
    cnv.itemconfig(o, fill=rgb[counter % len(rgb)])
    counter += 10
    cnv.move(o, vx, vy)

    x1, y1, x2, y2 = cnv.coords(o)
    if y1 > H - a:
        vy = -vy
    if y1 < 0:
        vy = -vy
    if x1 < 0:
        vx = -vx
    if x1 > W - a:
        vx = -vx
    cnv.after(10, animate)


animate()

mainloop()
