import tkinter.messagebox
from tkinter import *
import sqlite3

root = Tk()
root.title("Registration Forum")
root.iconbitmap("agree_0.ico")
root.geometry("800x600")
root.resizable(width=False, height=False)
 # bg = PhotoImage(file="starysky.png")
#Creating a database
"""database = sqlite3.connect('registration.db')
#Creating Cursor
cursor = database.cursor()"""
'''
#Creating Table
cursor.execute("""Create Table Information (
full_name text,
username text,
password text
)""")
'''
'''
def register():
    # Creating a database
    database = sqlite3.connect('registration.db')
    # Creating Cursor
    cursor = database.cursor()
    #Inserting Data Into Table
    cursor.execute("Insert Into Information Values (:name, :username, :password)",
                   {
                       'name': name_entry.get(),
                       'username': username_entry.get(),
                       'password': password_entry.get()
                   })
    cursor.execute("Select *,oid From Information")
    data = cursor.fetchall()
    print(data)
    # Commiting Changes
    database.commit()
'''
# Creating Canvas
my_canvas = Canvas(root, width=800, height=600, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)
#Setting Canvas Image
# my_canvas.create_image(0,0, image=bg, anchor="nw")
#Creating Label In Canvas
my_canvas.create_text(400, 60, text="CREATE AN ACCOUNT", font=("arial",30,'bold'), fill="white")
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

"""# drop down menu for gender

gender = ["Male", "Female", "Others", "Not to say"]
indicator = StringVar()
indicator.set("Male")
dropper = OptionMenu(root, indicator, *gender)
dropper.pack()
# dropper.config(bg="green")"""


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
mainloop()