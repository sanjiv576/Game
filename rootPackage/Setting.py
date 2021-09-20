from tkinter import *
from rootPackage.control1 import open_control


def open_setting():
    root = Toplevel()
    root.title("Setting")
    root.iconbitmap("sponge.ico")
    root.geometry("800x600")
    root.resizable(width=False, height=False)
    bg = PhotoImage(file="island3.png")

    # Creating Canvas
    my_canvas = Canvas(root, width=800, height=600, highlightthickness=0)
    my_canvas.pack(fill="both", expand=False)

    #Setting Canvas Image
    my_canvas.create_image(0,0, image=bg, anchor="nw")
    #n, ne, e, se, s, sw, w, nw, or center

    def exit_setting():
        root.destroy()

    #Creating Control Button
    control_button = Button(root, text="CONTROL", bg="#59c2dc", bd=0, fg="white", font=("arial", 15, 'bold'), width=15, height=2, command=open_control)
    control_window = my_canvas.create_window(310, 150, anchor="nw", window=control_button)

    #Creating Sound Button
    sound_button = Button(root, text="SOUND", bg="#59c2dc", bd=0, fg="white", font=("arial", 15, 'bold'), width=15, height=2)
    sound_window = my_canvas.create_window(310, 250, anchor="nw", window=sound_button)

    #Creating Highscore Button
    highscore_button = Button(root, text="HIGHSCORE", bg="#59c2dc",bd=0, fg="white", font=("arial", 15, 'bold'), width=15, height=2)
    highscore_window = my_canvas.create_window(310, 350, anchor="nw", window=highscore_button)

    #Creating Back Button
    back_button = Button(root, text="BACK", bg="#59c2dc",bd=0, fg="white", font=("arial", 15, 'bold'), width=15, height=2, command=exit_setting)
    back_window = my_canvas.create_window(310, 450, anchor="nw", window=back_button)

    root.mainloop()
