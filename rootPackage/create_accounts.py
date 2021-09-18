import tkinter
import tkinter.messagebox
from tkinter import messagebox
from tkinter import *
import sqlite3
def link():

    root = tkinter.Toplevel()
    root.title("Registration Forum")
    root.iconbitmap("agree_0.ico")
    root.geometry("800x600")
    root.resizable(width=False, height=False)
    root.configure(bg="green")
    bg = PhotoImage(file="spongebob.png")


    # ----------------------------database use from here------------------------------------
    connet_me = sqlite3.connect("Test.db")
    cur = connet_me.cursor()
    """   
    # creating table
    cur.execute('''CREATE TABLE ourTable(
                                         full_name text,
                                         username text,
                                         password text)''')
    print("Table has been created successfully.")"""

    connet_me.commit()
    connet_me.close()

    # Creating Canvas
    my_canvas = Canvas(root, width=800, height=600, highlightthickness=0)
    my_canvas.pack(fill="both", expand=True)

    my_canvas.create_image(0, 0, image=bg, anchor="nw")
    #Setting Canvas Image
    #  my_canvas.create_image(0,0, image=backGround, anchor="nw")
    #Creating Label In Canvas
    my_canvas.create_text(400, 60, text="CREATE AN ACCOUNT", font=("arial",30,'bold'), fill="blue")
    my_canvas.create_text(300, 140, text="FULL NAME", font=("helvetica",13, 'bold'), fill="grey")
    my_canvas.create_text(300, 235, text="USERNAME", font=("helvetica",13,'bold'), fill="grey")
    my_canvas.create_text(300, 330, text="PASSWORD", font=("helvetica",13,'bold'), fill="grey")
    my_canvas.create_text(340, 425, text="CONFIRM PASSWORD", font=("helvetica",13,'bold'), fill="grey")
    #Defining Entry Boxes
    name_entry = Entry(root, bd=0.5, bg="black", fg="white", font=("cambria", 22, 'italic'), insertbackground="white")
    username_entry = Entry(root, bd=0.5, bg="black", fg="white", font=("cambria", 22, 'italic'), insertbackground="white")
    password_entry = Entry(root, bd=0.5, bg="black", fg="white", font=("cambria", 22, 'italic'), show="*", insertbackground="white")
    confirm_password_entry = Entry(root, bd=0.5, bg="black", fg="white", font=("cambria", 22, 'italic'), show="*", insertbackground="white")
    #Adding Entry Boxes To Canvas
    nam_window = my_canvas.create_window(250, 150,anchor="nw", window=name_entry)
    username_window = my_canvas.create_window(250, 245,anchor="nw", window=username_entry)
    password_window = my_canvas.create_window(250, 340,anchor="nw", window=password_entry)
    confirm_password_window = my_canvas.create_window(250, 435,anchor="nw", window=confirm_password_entry)

    # drop down menu for gender

    gender = ["Male", "Female", "Others", "Not to say"]
    indicator = StringVar()
    indicator.set("Male")
    dropper = OptionMenu(root, indicator, *gender)
    dropper.pack()
    # dropper.config(bg="green")


    def register():
        if name_entry.get() == "" and username_entry.get() == "" and password_entry.get() == "" and confirm_password_entry.get() == "":
            tkinter.messagebox.showinfo("INVALID DETAILS", "Please Enter Name,Username,Password Correctly")
        elif name_entry.get() == "" and username_entry.get() == "" and password_entry.get() == "":
            tkinter.messagebox.showinfo("INVALID DETAILS", "Please Enter Name,Username,Password Correctly")
        elif name_entry.get() == "" and username_entry.get() == "" and confirm_password_entry.get() == "":
            tkinter.messagebox.showinfo("INVALID DETAILS", "Please Enter Name,Username,Confirm Password Correctly")
        elif name_entry.get() == "" and username_entry.get() == "":
            tkinter.messagebox.showinfo("INVALID DETAILS", "Please Enter Name,Username Correctly")
        elif username_entry.get() == "" and password_entry.get() == "":
            tkinter.messagebox.showinfo("INVALID DETAILS", "Please Enter Username,Password Correctly")
        elif name_entry.get() == "" and password_entry.get() == "":
            tkinter.messagebox.showinfo("INVALID DETAILS", "Please Enter Name,Password Correctly")
        elif password_entry.get() == "" and confirm_password_entry.get() == "":
            tkinter.messagebox.showinfo("INVALID DETAILS", "Please Enter Your Password Correctly")
        elif password_entry.get() != confirm_password_entry.get():
            tkinter.messagebox.showinfo("INVALID PASSWORD", "Please Enter Your Password Correctly!")
        elif name_entry.get() == "":
            tkinter.messagebox.showinfo("NAME EMPTY", "Please Enter Your Name Correctly!")
        elif username_entry.get() == "":
            tkinter.messagebox.showinfo("USERNAME EMPTY", "Please Enter Your Username Correctly!")
        else:
            connet_me = sqlite3.connect("Test.db")
            cur = connet_me.cursor()
            cur.execute("INSERT INTO ourTable VALUES(:full_name, :username_provided, :password_provided)",
                        {'full_name':name_entry.get(),'username_provided':username_entry.get(),
                         'password_provided':password_entry.get()})
            print("Data have been inserted successfully.")
            connet_me.commit()
            connet_me.close()
            messagebox.showinfo("Registration Successfully.", "Your account has been created successfully.")



    #Creating Register Button
    register_button = Button(root, text="REGISTER", bd=3, bg="black", fg="red", font=("arial", 15, 'bold'), width=15, height=2, command=register)
    register_window = my_canvas.create_window(310, 500, anchor="nw", window=register_button)

    '''
    # Creating Label
    my_label = Label(root, image=bg)
    my_label.place(x=0, y=0,  relwidth=1, relheight=1)
    # Creating Account
    my_house = Label(root, text="Create An Account", Font=("arial", 40, "bold")
    my_house.pack(pady=40)
    '''
    #Commiting Changes
        #database.commit()

    root.mainloop()
