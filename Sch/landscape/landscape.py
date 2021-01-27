#!/bin/python3

from tkinter import *
from random import *
from libcolor import *

master = Tk()
# Window titlebar :)
master.title("Landscape")
W, H = 1000, 700
cnv = Canvas(master, width=W, height=H)
cnv.pack()

horizon_coord = 430

upper_skycolor = color(0, 153, 191)
lower_skycolor = color(115, 124, 255)

# drawing gradient sky background
count = -1
for i in lingrad_triple(upper_skycolor, lower_skycolor, horizon_coord):
    count += 1
    cnv.create_line(0, count, W-1, count, fill = i.to_hex())

# drawing THE SUN
cnv.create_oval(rect_mid(W//2, horizon_coord, 200, 200), fill = "#ff5e00", outline = "")

# drawing cool gradient clouds
upper_coloudcolor = color(136, 143, 225)
lower_cloudcolor = color(240, 251, 255)
cloudcolor = color(0, 0, 0)
n_clouds = 100

for i in range(n_clouds):
    x = randint(0, W)
    y = randint(0, horizon_coord)
    cloudcolor = pointgrad_triple(upper_coloudcolor, lower_cloudcolor, y, H - horizon_coord)
    cnv.create_oval(rect_mid(x, y, randint(50, 80), randint(80, 110)), fill=cloudcolor.to_hex(), outline='')

# Drawing the gradient ground background
upper_groundcolor = color(30, 175, 88)
lower_groundcolor = color(1, 56, 0)
count = -1
for i in lingrad_triple(upper_groundcolor, lower_groundcolor, H - horizon_coord):
    count += 1
    cnv.create_line(0, horizon_coord + count, W-1, horizon_coord + count, fill = i.to_hex())

# Drawing grass. Not much has changed here.
n_grass = 15000
for i in range(n_grass):
    x = randint(0, W)
    y = randint(horizon_coord, H)
    grass_color = choice(["green", "green1", "green2", "green3", "green4", "green", "green1", "green2", "green3", "green4", "green", "green1", "green2", "green3", "green4", "green", "green1", "green2", "green3", "green4", "green", "green1", "green2", "green3", "green4", "yellow"])
    cnv.create_line(rect_mid(x, y, randint(15, 25), randint(1, 2)), fill=grass_color, width=2)


mainloop()
