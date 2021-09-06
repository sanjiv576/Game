from tkinter import *
from tkinter import messagebox
import sys
from Credit import open_credit
from Setting import open_setting
root = Tk()
root.title("Our Game")
root.iconbitmap("sponge.ico")
root.geometry("800x600")
root.resizable(width=False, height=False)
bg = PhotoImage(file="island.png")

# Creating Canvas
my_canvas = Canvas(root, width=800, height=600, highlightthickness=0)
my_canvas.pack(fill="both", expand=False)

#Setting Canvas Image
my_canvas.create_image(0,0, image=bg, anchor="nw")
#n, ne, e, se, s, sw, w, nw, or center

#Defining Exit Button
def alert():
    sure_exit = messagebox.askyesno("Exit", "Are You Sure To Exit The Game?")

    if sure_exit == 1:
        sys.exit()

    else:
        pass


#Creating Start Button
start_button = Button(root, text="START", bg="#59c2dc", bd=0, fg="white", font=("arial", 15, 'bold'), width=15, height=2)
start_window = my_canvas.create_window(310, 150, anchor="nw", window=start_button)

#Creating Setting Button
setting_button = Button(root, text="SETTING", bg="#59c2dc", bd=0, fg="white", font=("arial", 15, 'bold'), width=15, height=2, command=open_setting)
setting_window = my_canvas.create_window(310, 250, anchor="nw", window=setting_button)

#Creating Credit Button
credit_button = Button(root, text="CREDIT", bg="#59c2dc",bd=0, fg="white", font=("arial", 15, 'bold'), width=15, height=2, command=open_credit)
credit_window = my_canvas.create_window(310, 350, anchor="nw", window=credit_button)

#Creating Exit Button
exit_button = Button(root, text="EXIT", bg="#59c2dc",bd=0, fg="white", font=("arial", 15, 'bold'), width=15, height=2, command=alert)
exit_window = my_canvas.create_window(310, 450, anchor="nw", window=exit_button)

mainloop()