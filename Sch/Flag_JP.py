from tkinter import*
master=Tk()
cnv=Canvas(master, width=600, height=400)
cnv.pack()

cnv.create_rectangle(100, 100, 500, 400, width=4, outline="black", fill="white")
cnv.create_oval(200, 150, 400, 350, width=6, outline="red", fill="red")
mainloop()
