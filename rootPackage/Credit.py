from tkinter import *

def open_credit():
    root = Toplevel()
    root.title("Credits")
    root.iconbitmap("sponge.ico")
    root.geometry("800x600")
    root.resizable(width=False, height=False)
    bg = PhotoImage(file="island2.png")

    # Creating Canvas
    my_canvas = Canvas(root, width=800, height=600, highlightthickness=0)
    my_canvas.pack(fill="both", expand=False)

    #Setting Canvas Image
    my_canvas.create_image(0,0, image=bg, anchor="nw")

    #Creating Label In Canvas
    my_canvas.create_text(425, 200, text="""
    All The Credit For Our Billion Dollar Game 
        Goes To Our Core Team Members. 
    """, font=("arial",25,'bold'), fill="black")

    my_canvas.create_text(425, 350, text=""" 
    Subifa Maharjan
    Nishant Raj Dahal 
    Sanjiv Shrestha 
    Nitesh Poudel
    """, font=("arial",23,'bold'), fill="black",)

    root.mainloop()
