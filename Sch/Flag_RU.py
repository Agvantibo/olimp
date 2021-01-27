from tkinter import*
master=Tk()
cnv=Canvas(master, width=600, height=400)
cnv.pack()
w = 500
h = 300
cnv.create_rectangle(50, 50, 550, 150, width=4, outline="black", fill="white")
cnv.create_rectangle(50, 150, 550, 250, width=4, outline="black", fill="blue")
cnv.create_rectangle(50, 250, 550, 350, width=4, outline="black", fill="red")

mainloop()
