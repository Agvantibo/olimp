from tkinter import*

master=Tk()
s=100
w=6*s
h=4*s
cnv=Canvas(master, width=w, height=h)
cnv.pack()

def draw_t(x, y, direction, colour):
    cnv.create_rectangle(x * s, y * s, (x + 1)*s, (y + 1)*s, fill=colour)
    
    if direction != "d":
        cnv.create_rectangle(x*s, (y-1)*s, (x+1)*s, y*s, fill=colour)
    if direction != "u":
        cnv.create_rectangle(x*s, (y+1)*s, (x+1)*s, (y+2)*s, fill=colour)
    if direction != "l":
        cnv.create_rectangle((x+1)*s, y*s, (x+2)*s, (y+1)*s, fill=colour)
    if direction != "r":
        cnv.create_rectangle((x-1)*s, y*s, x*s, (y+1)*s, fill=colour)


draw_t(4, 0, "d", "red")
draw_t(3, 3, "u", "blue")
draw_t(2, 1, "l", "green")
draw_t(0, 2, "r", "yellow")

mainloop()
