from tkinter import *
from random import *
from time import sleep
root = Tk()
 
c = Canvas(root, width=500, height=750, bg='white')
c.pack()
img = PhotoImage(file = "einstein.png")
c.create_image(0, 0, anchor = NW, image=img)

redpool = ["red", "red4",  "salmon", "magenta2", "violetred4"]
rainpool = ["red", "orange", "green", "yellow", "lightblue", "blue", "magenta"]

horncolor1=choice(redpool)
horncolor2=choice(redpool)
c.create_polygon(155, 160, 130, 175, 
109, 150, 115, 110, 120, 132, outline=horncolor1,  fill=horncolor1)
c.create_polygon(275, 170, 300, 185, 
314, 150, 285, 110, 291, 132, outline=horncolor2,  fill=horncolor2)

c.create_polygon(80, 395, 0, 380, 0, 405, outline = "white", fill = "white")
c.create_polygon(390, 390, 500, 435, 500, 395, outline = "white", fill = "white")
c.create_oval(420, 380, 530, 445, outline = "white", fill = "white")
c.create_oval(-30, 370, 60, 420, outline = "white", fill = "white")

for i in range(20):
    col = choice(rainpool)
    w1 = randint(0, 750)
    h1 = randint(0, 750)
    c.create_oval(w1, h1, w1 + 50, h1 + 50, outline=col, fill=col)

happinessRay1x = randint(0, 680)
happinessRay2x = randint(0, 680)
c.create_polygon(happinessRay1x, 750, happinessRay1x + 70, 750, 136, 310, outline = "yellow", fill = "yellow")
c.create_polygon(happinessRay2x, 750, happinessRay2x + 70, 750, 259,  310, outline = "yellow", fill = "yellow")

root.mainloop()
