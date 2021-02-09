#!/bin/python3
from tkinter import *
from random import *

master = Tk()
W, H = 800, 600
cnv = Canvas(master, width=W, height=H)
cnv.pack()

H1 = int(H * 0.319)

cnv.create_rectangle(0, 0, W, H1, fill='light sky blue', outline='')

def colour_code(r, g, b): ## 255, 255, 0 (жёлтый) -> '#ffff00'
    d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    #print(r, g, b)
    return '#'+d[r//16]+d[r%16]+d[g//16]+d[g%16]+d[b//16]+d[b%16]

for i in range(2000): # clouds
    y = randint(0, H1)
    R = int(5 + (H1 - y) / H1 * 20)
    x = randint(-R, W + R)
##    if randint(1, 3) == 1:
##        colour = 'light sky blue'
##    else:
##        colour = 'thistle2'
    if randint(1, 4) == 1:
        colour = 'light sky blue'
    else:
        r, g, b = 216, 191, 216
        a = 1 - 0.5 * y / H1 # a плавно меняется от 1 до 0.5
        r, g, b = int(r * a), int(g * a), int(b * a) # плавно затемняем синий
        colour = colour_code(r, g, b)
    cnv.create_oval(x-R, y-R/2, x+R, y+R/2, fill=colour, outline='')

h = 10
cnv.create_rectangle(0, H1 - h, W, H1, fill='SeaGreen1', outline='')

for i in range(200): # trees
    R = randint(10, 25)
    x = randint(-R, W+R)
    y = randint(H1-h, H1)
    #colour = 'SeaGreen'+str(randint(1,3))
    # случайный цвет в промежутке
    colour = colour_code(randint(32, 46), randint(139, 178), randint(87, 170))
    cnv.create_oval(x-R, y-R, x+R, y+R, fill=colour, outline='')

#sea
r1, g1, b1 = 0, 0, 128
r2, g2, b2 = 0, 0, 255
cnv.create_rectangle(0, H1, W, H, fill='blue2', outline='')
for i in range(H1, H):
    colour = colour_code(0, 0, int(128 + 127 * (i - H1)/(H - H1))) # градиент
    cnv.create_line(0, i, W, i, fill=colour)

for i in range(1000): # tree reflections
    y = randint(H1+1, H1 + 3*h)
    L = randint(3, 8)
    x = randint(-L, W+L)
    if randint(1, 2) == 1:
        colour = 'light sea green'
    else:
        colour = 'medium sea green'
    cnv.create_line(x-L, y, x+L, y, fill=colour, width=2)

for i in range(10000): # water
    y = randint(H1, H)
    L = int(4 + 16 * (y - H1) / (H - H1))
    w = 1 + L / 10
    x = randint(-L, W + L)
    c = randint(1, 3)
    if c == 1:
        colour = 'navy'
    elif c == 2:
        colour = 'turquoise1'
    else:
        colour = 'dodger blue'
    cnv.create_line(x-L/2, y, x+L/2, y, width=w, fill=colour)

for i in range(50): # birds
    x = randint(0, W)
    y = randint(0, H1-h)
    r = randint(2, 4)
    cnv.create_line(x, y, x-r, y-r, fill='SlateBlue4')
    cnv.create_line(x-r, y-r, x-3*r, y-2*r, fill='SlateBlue4')
    cnv.create_line(x, y, x+r, y-r, fill='SlateBlue4')
    cnv.create_line(x+r, y-r, x+3*r, y-2*r, fill='SlateBlue4')

pts = [300, 330, 500, 330, 475, 355, 350, 355] # boat
cnv.create_polygon(pts, fill='thistle1', outline='')

cnv.create_line(425, 330, 425, 180, fill='thistle1', width=6)
cnv.create_line(300, 330, 425, 180, fill='white')
cnv.create_line(500, 330, 425, 180, fill='white')

cnv.create_polygon(308, 320, 418, 188, 418, 320, fill='white')
cnv.create_polygon(496, 320, 432, 192, 432, 320, fill='white')
cnv.create_line(308, 320, 496, 320, fill='white')

pts = [422, 180, 422, 170, 445, 170, 440, 174, 445, 180] # jump
cnv.create_polygon(pts, fill='yellow', outline='')

for i in range(200): # reflection boat 1
    x = randint(300, 500)
    y = randint(355, 405)
    L = int(4 + 16 * (y - H1) / (H - H1))
    w = 1 + L / 10
    cnv.create_line(x-L/2, y, x+L/2, y, width=w, fill='LightBlue1')

for i in range(100): # reflection boat 2
    x = randint(300, 500)
    y = randint(405, 455)
    L = int(4 + 16 * (y - H1) / (H - H1))
    w = 1 + L / 10
    cnv.create_line(x-L/2, y, x+L/2, y, width=w, fill='LightBlue1')

for i in range(5): # reflection jump
    x = randint(425, 445)
    y = randint(445, 455)
    L = int(4 + 16 * (y - H1) / (H - H1))
    w = 1 + L / 10
    cnv.create_line(x-L/2, y, x+L/2, y, width=w, fill='gold2')

mainloop()
