from tkinter import *
from tkinter import messagebox

row_num = 0


def create_my_account():
    register = Tk()
    register.title("Registration Forum")
    register.iconbitmap("agree_0.ico")
    register.geometry("740x749")
    register.configure(bg="#CDC8B1")  # #CDC8B1 = silkcorn color
    '''
    create_image = PhotoImage(file="account_create.png")
    Label(register, image=create_image)
    #create_image.grid(row=1, column=2)

    img_button = Button(register, image=create_image)
    img_button.grid(row=1, column=3)'''

    # frame created to maintain buttons and labels in a systematic arrangement
    my_frame = Frame(register, bg="#CDC8B1")
    my_frame.pack()

    # function for show message

    def show_message():
        if f_nam_entry.get() == "" and l_nam_entry.get() == "" and user_name_entry.get() == "" and \
                password_entry.get() == "" and conf_password_entry.get() == "":
            messagebox.showwarning("Warning Encountered ! ", "Please , fill all boxes.")
        elif f_nam_entry.get() == "":
            messagebox.showwarning("Warning Encountered ! ", "Please , fill first name box.")
        elif l_nam_entry.get() == "":
            messagebox.showwarning("Warning Encountered ! ", "Please , fill last name box.")
        elif user_name_entry.get() == "":
            messagebox.showwarning("Warning Encountered ! ", "Please , fill  username box.")

        elif password_entry.get() == "":
            messagebox.showwarning("Warning Encountered ! ", "Please , fill  password box.")

        elif conf_password_entry.get() == "":
            messagebox.showwarning("Warning Encountered ! ", "Please , fill  confirm password box.")
        elif conf_password_entry.get() != password_entry.get():  # checking password and confirm password match or not
            messagebox.showwarning("Warning Encountered ! ",
                                   "Password and Confirm password do not match. Please, enter again.")
        else:
            messagebox.showinfo("Account Created", "Congratulation! Your account has been created successfully.")
            register.destroy()

    # function to show msg for exit window
    def show_quit():
        user_respond = messagebox.askokcancel("Warning !", "Do you want to quit ? ")
        if user_respond == 1:
            register.destroy()

    # function for empty labels

    def empty():
        global row_num
        if row_num <= 30:
            empty_label = Label(my_frame, text="", bg="#CDC8B1")
            empty_label.grid(row=row_num)
            row_num += 2

    # labels
    empty()
    heading_label = Label(my_frame, text="CREATE AN ACCOUNT", font=("copperplate", 32, 'bold'),
                          bg="#CDC8B1", fg="green")
    heading_label.grid(row=1, column=1)
    # rows = 2, 3 are left for empty for future use
    empty()
    f_name = Label(my_frame, text="First Name :", bg="#CDC8B1", font=("Times New Roman", 21, 'bold'))
    f_name.grid(row=3, column=0)
    empty()
    l_name = Label(my_frame, text="Last Name :", bg="#CDC8B1", font=("Times New Roman", 21, 'bold'))
    l_name.grid(row=5, column=0)
    empty()
    gender_label = Label(my_frame, text="Gender :", bg="#CDC8B1", font=("Times New Roman", 21, 'bold'))
    gender_label.grid(row=7, column=0)
    empty()
    user_name = Label(my_frame, text="Username :", bg="#CDC8B1", font=("Times New Roman", 21, 'bold'))
    username = StringVar()
    user_name.grid(row=9, column=0)
    empty()
    password_label = Label(my_frame, text="Password :", bg="#CDC8B1", font=("Times New Roman", 21, 'bold'))
    password = StringVar()
    password_label.grid(row=11, column=0)
    empty()
    conf_password_label = Label(my_frame, text="Confirm Password :", bg="#CDC8B1", font=("Times New Roman", 21, 'bold'))
    confirm_password = StringVar()
    conf_password_label.grid(row=13, column=0)
    empty()

    # button defined
    submit_button = Button(my_frame, text="SUBMIT", highlightbackground="green", command=show_message,
                           font=("Century Gothic", 24, 'bold'))
    submit_button.grid(row=15, column=1, ipadx=18, ipady=3)
    empty()
    exit_button = Button(my_frame, text="EXIT", highlightbackground="red", command=show_quit,
                         font=("Century Gothic", 24, 'bold'))
    exit_button.grid(row=17, column=1, ipadx=18, ipady=3, rowspan=2)

    # drop down menu for gender

    gender = ["Male", "Female", "Others", "Not to say"]
    indicator = StringVar()
    indicator.set("Male")
    dropper = OptionMenu(my_frame, indicator, *gender)
    dropper.grid(row=7, column=1, ipadx=60, ipady=3)
    # dropper.config(bg="green")

    # drop down menu for birthday date
    """date = []
    for i in range(1920, 2022):
        date.append(str(i))

    date_indicate = StringVar()
    date_indicate.set("2021")
    drop = OptionMenu(my_frame, date_indicate, *date)
    drop.grid(row=21, column=1)

    month = []
    for i in range(1, 31):
        month.append(str(i))

    month_indicate = StringVar()
    month_indicate.set("1")
    drop = OptionMenu(my_frame, month_indicate, *date)
    drop.grid(row=21, column=2)"""

    # entry fields
    f_nam_entry = Entry(my_frame, bg="#474747", fg="white", font=("cambria", 16, 'italic'))
    f_nam_entry.grid(row=3, column=1, ipadx=60, ipady=3)

    l_nam_entry = Entry(my_frame, bd=2, bg="#FFD39B", font=("cambria", 16, 'italic'))
    #  #FFD39B= burlywood1
    l_nam_entry.grid(row=5, column=1, ipadx=60, ipady=3)

    user_name_entry = Entry(my_frame, bd=2, bg="#474747", fg="white", textvariable=username,
                            font=("cambria", 16, 'italic'))
    user_name_entry.grid(row=9, column=1, ipadx=60, ipady=3)

    password_entry = Entry(my_frame, bd=2, bg="#FFD39B", textvariable=password, show="•",
                           font=("cambria", 16, 'italic'))
    password_entry.grid(row=11, column=1, ipadx=60, ipady=3)

    conf_password_entry = Entry(my_frame, bd=2, bg="#474747", fg="white",
                                show="•", font=("cambria", 16, 'italic'))
    conf_password_entry.grid(row=13, column=1, ipadx=60, ipady=3)

    # Slider added
    def geometry_change():
        register.geometry(str(length_scale.get()) + "x" + str(height_scale.get()))

    empty()
    height_scale = Scale(my_frame, from_=100, to=1000, orient=VERTICAL)
    height_scale.grid(row=19, column=3)
    height_scale.set(749)  # this set function shows first geometry of height
    Label(my_frame, text="Height", bg="#CDC8B1").grid(row=20, column=3)
    empty()
    length_scale = Scale(my_frame, from_=50, to=1500, orient=HORIZONTAL)
    length_scale.grid(row=19, column=0)
    Label(my_frame, text="Length", bg="#CDC8B1").grid(row=20, column=0)
    length_scale.set(740)  # this shows first geometry of length of the window

    geometry_change_btn = Button(my_frame, text="Change window size", command=geometry_change,
                                 padx=9, pady=9, highlightbackground="yellow")
    geometry_change_btn.grid(row=19, column=1)

    register.mainloop()