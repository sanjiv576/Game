from tkinter import *
import sqlite3
from tkinter import messagebox
window = Tk()
window.title("Login Window")
window.configure(bg="#6E6E6E")  # #6E6E6E = gray43
window.geometry("400x700")
# window.iconbitmap("")
# handling database starts
# creating a database or connect to one
connector = sqlite3.connect("login_details.db")
# creating a cursor
blinker = connector.cursor()
'''# creating a table
blinker.execute("""CREATE TABLE login_details(
               username text
               password string)""")
print("Table has been created successfully.")'''
# GUI starts
msg = Label(window, text="USER lOGIN", font=("copperplate", 44), fg="orange", bg="#6E6E6E")
msg.pack(ipadx=60, ipady=30)
# image insertion
my_img = PhotoImage(file="loginManager.png")
Label(window, image=my_img, bg="#6E6E6E").pack()

# function for showing username and password

def have_an_account():

    if username_entry.get() == "" and password_entry.get() == "":
        messagebox.showwarning("Warning !", "Please, fill both username and password boxes.")
    elif password_entry.get() == "":
        messagebox.showwarning("Warning !", "Please, fill password box.")
    elif username_entry.get() == "":
        messagebox.showwarning("Warning !", "Please, fill username box.")
    else:
        print("User name : ", username_entry.get())
        print("Password : ", password_entry.get())


# username -- label, entry field
username_label = Label(window, text="User Name", font=("courier", 17), fg="white", bg="#6E6E6E")
username = StringVar()   # StringVar() is used to hold string values and use in textvariable
username_label.pack(ipadx=10, ipady=10)

username_entry = Entry(window, bg="orange", textvariable=username)
username_entry.pack()

# password -- label, entry field
password_label = Label(window, text="Password", font=("courier", 17), fg="white", bg="#6E6E6E")
password = StringVar()
password_label.pack(ipadx=10, ipady=10)

password_entry = Entry(window, bg="orange", textvariable=password, show="•")  # password shows in • hidden form
password_entry.pack(ipadx=2, ipady=2)

# function to open new window and create my new account

# function created to exit the window
def exit_window():
    response_from_user = messagebox.askyesno("Alert !", "Do you want to quit ? ")  # yes button = 1, no button = 0
    if response_from_user == 1:
        #my_frame.destroy()
        sys.exit()   # close the window
    else:
        pass

# function to create empty rows and columns
countMe = 0
def empty_line():
    global countMe
    if countMe == 2:
        empty_label = Label(my_frame, text="OR", bg="#6E6E6E", font=("courier", 17), fg="white")
        empty_label.grid(row=countMe, column=1)
        countMe += 2
    elif countMe <= 22:
        empty_label = Label(my_frame, text="", bg="#6E6E6E", font=("courier", 17), fg="white")
        empty_label.grid(row=countMe, column=1)
        countMe += 2
    else:
        pass

# frame created to maintain buttons and labels in a systematic arrangement
my_frame = Frame(window, bg="#6E6E6E")
my_frame.pack()

# buttons defined inside the frame
empty_line()
login_button = Button(my_frame, text="Login", highlightbackground="blue", font=("courier", 17),
                      fg="white", padx=10, pady=6, command=have_an_account)
login_button.grid(row=1, column=1)
empty_line()
noAccount_button = Button(my_frame, text="Don't have an account ?", highlightbackground="green",
                           font=("courier", 17), fg="white", padx=10, pady=8)
noAccount_button.grid(row=3, column=1)
empty_line()
quit_button = Button(my_frame, text="Quit", highlightbackground="red", relief=RAISED,
                          font=("courier", 17), fg="white", padx=10, pady=8, command=exit_window)
quit_button.grid(row=5, column=1)
empty_line()
"""official_use_btn = Button(my_frame, text="For only official users", highlightbackground="#483D8B",
                          command=create_my_account, font=("courier", 17), fg="black", padx=10, pady=8)
official_use_btn.grid(row=7, column=1)"""

"""# labels created inside the frame to maintain space between two buttons
empty_label = Label(my_frame, text="", bg="#6E6E6E", font=("courier", 17), fg="white")
empty_label.grid(row=0, column=1)
empty_label1 = Label(my_frame, text="OR", bg="#6E6E6E", font=("courier", 17), fg="white")
empty_label1.grid(row=2, column=1)
empty_label2 = Label(my_frame, text="", bg="#6E6E6E", font=("courier", 17), fg="white")
empty_label2.grid(row=4, column=1)
empty_label3 = Label(my_frame, text="", bg="#6E6E6E", font=("courier", 17), fg="white")
empty_label3.grid(row=4, column=1)
"""
connector.commit()
connector.close()

window.mainloop()
