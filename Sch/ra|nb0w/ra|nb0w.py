#!/bin/python3
from tkinter import *
from libcolor import *
master = Tk()
W, H = 1187, 300
cnv = Canvas(master, width=W, height=H)
cnv.pack()
color = color(255, 0, 0)

for i in range(255):
    cnv.create_line(i, 0, i, H - 1, fill = color.to_hex())
    color.g += 1

for i in range(255, 511):
    cnv.create_line(i, 0, i, H - 1, fill = color.to_hex())
    color.r -= 1

for i in range(511, 766):
    cnv.create_line(i, 0, i, H - 1, fill = color.to_hex())
    color.b += 1

for i in range(766, 977):
    cnv.create_line(i, 0, i, H - 1, fill = color.to_hex())
    color.g -= 1

for i in range(977, 1188):
    cnv.create_line(i, 0, i, H - 1, fill = color.to_hex())
    color.r += 1


mainloop()
