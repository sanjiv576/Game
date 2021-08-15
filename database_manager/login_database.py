from tkinter import *
import sqlite3

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
# GUI starts from here
msg = Label(window, text="USER lOGIN", font=("copperplate", 44), fg="orange", bg="#6E6E6E")
msg.pack(ipadx=60, ipady=30)
# image insertion
my_img = PhotoImage(file="loginManager.png")
Label(window, image=my_img).pack()


# function for showing username and password
def have_an_account():
    print("User name : ", username_entry.get())
    print("Password : ", password_entry.get())


# username -- label, entry field
username_label = Label(window, text="User Name", font=("courier", 17), fg="white", bg="#6E6E6E")
username = StringVar()
username_label.pack(ipadx=10, ipady=10)
username_entry = Entry(window, bg="orange", textvariable=username)
username_entry.pack()
# password -- label, entry field
password_label = Label(window, text="Password", font=("courier", 17), fg="white", bg="#6E6E6E")
password = StringVar()
password_label.pack(ipadx=10, ipady=10)
password_entry = Entry(window, bg="orange", textvariable=password, show="•")  # password shows in • hidden form
password_entry.pack(ipadx=2, ipady=2)

# frame created
my_frame = Frame(window, bg="#6E6E6E")
my_frame.pack()
# buttons defined inside the frame
empty_label = Label(my_frame, text="", bg="#6E6E6E", font=("courier", 17), fg="white")
empty_label.grid(row=0, column=1)
login_button = Button(my_frame, text="Login", highlightbackground="blue", font=("courier", 17),
                      fg="white", padx=10, pady=6, command=have_an_account)
login_button.grid(row=1, column=1)
empty_label1 = Label(my_frame, text="OR", bg="#6E6E6E", font=("courier", 17), fg="white")
empty_label1.grid(row=2, column=1)
noAccount_button = Button(my_frame, text="Don't have an account ?", highlightbackground="green",
                          font=("courier", 17), fg="white", padx=10, pady=8)
noAccount_button.grid(row=3, column=1)
empty_label2 = Label(my_frame, text="", bg="#6E6E6E", font=("courier", 17), fg="white")
empty_label2.grid(row=4, column=1)
connector.commit()  # commit change --- saving the info
connector.close()  # closing connection between database and above table
window.mainloop()

