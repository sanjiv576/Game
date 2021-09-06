from tkinter import *
#def open_control():
root = Tk()
root.title("Credits")
root.iconbitmap("sponge.ico")
root.geometry("800x600")
root.resizable(width=False, height=False)
bg = PhotoImage(file="island2.png")
bg1 = PhotoImage(file="arrowkey.png")

# Creating Canvas
my_canvas = Canvas(root, width=800, height=600, highlightthickness=0)
my_canvas.pack(fill="both", expand=False)

#Setting Canvas Image
my_canvas.create_image(0,0, image=bg, anchor="nw")

#Setting Canvas Image
my_canvas.create_image(150,200, image=bg1)

#Creating Label In Canvas
my_canvas.create_text(420, 160, text="""
------------------ Moves The Character Up
""", font=("arial",20,'bold'), fill="black")

my_canvas.create_text(510, 230, text="""
------------------ Moves The Character Down
""", font=("arial",20,'bold'), fill="black")

my_canvas.create_text(510, 230, text="""
|
|
------------------ Moves The Character Down
""", font=("arial",20,'bold'), fill="black")

mainloop()
