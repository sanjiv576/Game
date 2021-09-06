from tkinter import *
def open_control():
    root = Toplevel()
    root.title("Credits")
    root.iconbitmap("sponge.ico")
    root.geometry("800x600")
    root.resizable(width=False, height=False)
    bg = PhotoImage(file="island2.png")
    bg1 = PhotoImage(file="arrowkey2.png")

    # Creating Canvas
    my_canvas = Canvas(root, width=800, height=600, highlightthickness=0)
    my_canvas.pack(fill="both", expand=False)

    #Setting Canvas Image
    my_canvas.create_image(0,0, image=bg, anchor="nw")

    #Setting Arrow Image
    my_canvas.create_image(0,0, image=bg1, anchor="nw")


    mainloop()
