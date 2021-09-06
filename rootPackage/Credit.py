from tkinter import *

def open_credit():
    root = Toplevel()
    root.title("Credits")
    root.iconbitmap("sponge.ico")
    root.geometry("800x600")
    root.resizable(width=False, height=False)
    bg = PhotoImage(file="island2.png")


    """, font=("arial",25,'bold'), fill="black")

    my_canvas.create_text(425, 350, text=""" 
    Subifa Maharjan
    Nishant Raj Dahal 
    Sanjiv Shrestha 
    Nitesh Poudel
    """, font=("arial",23,'bold'), fill="black",)

    mainloop()
