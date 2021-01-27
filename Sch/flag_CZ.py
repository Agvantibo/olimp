from tkinter import*
master=Tk()
cnv=Canvas(master, width=600, height=400)
cnv.pack()
cnv.create_rectangle(00, 00, 600, 200, width=4, outline="white", fill="white")
cnv.create_rectangle(000, 200, 600, 400, width=4, outline="red", fill="red")
cnv.create_polygon(00, 00, 200, 200, 000, 400, width=2, outline="blue", fill="blue")

mainloop()
