from tkinter import *
from random import *

##N = 100
##for i in range(N):
##    a = randint(10, 100)
##    print(a)

master = Tk()
W, H = 800, 600
cnv = Canvas(master, width=W, height=H)
cnv.pack()

cnv.create_rectangle(0, 0, W, H, fill='light sky blue', outline='')

n_clouds = 200
for i in range(n_clouds):
    x = randint(0, W)
    y = randint(0, H/2)
    s1 = 20
    s2 = 4
    r = (s2 - s1) / (H / 2) * y + s1
    c = randint(0, 1)
    if c == 0:
        colour = 'gray80'
    else:
        colour = 'light sky blue'
    cnv.create_oval(x-2*r, y-r, x+2*r, y+r, fill=colour, outline='')

cnv.create_rectangle(0, H/2, W, H, fill='green', outline='')

n_grass = 10000
for i in range(n_grass):
    x = randint(0, W)
    y = randint(H/2, H)
    s1=1
    s2=20
    l = (s2 - s1) / (H / 2) * y + s1
    c = randint(0, 2)
    if c == 0:
        colour = 'green2'
    elif c == 1:
        colour = 'green3'
    else:
        colour = 'green4'
    cnv.create_line(x, y, x, y-l, fill=colour, width=2)


mainloop()
