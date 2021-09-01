
from tkinter import *
from tkinter.font import *
from rootPackage.create_accounts import link

def terms_and_conditions():

    agreement = Toplevel()
    agreement.title("Terms and Conditions")
    agreement.geometry("800x700")
    agreement.iconbitmap("agree_0.ico")
    agreement.configure(bg="silver")

    # using different fonts for different headings
    myFont = Font(size=20, weight="bold")


    # function created to hide this module and reveal main login window
    def close():
        agreement.withdraw()
        link()

        #create_my_account()


    # function for agree
    def agree():
        response = val.get()
        if response == "On":
            continue_button = Button(agreement, text="Continue", highlightbackground="yellow",
                                     command=close, font=("Gothic", 20), padx=9, pady=9)

            continue_button.pack()


    # files handling and labelling
    terms_and_condition_label = Label(agreement, text="Terms and Conditions", bg="black", fg="white")
    terms_and_condition_label['font'] = myFont
    terms_and_condition_label.pack()


    agreement_t = """
    Please read these Terms and Conditions carefully,
    before playing “Space Invaders ” operated by Guardians of the Galaxy.
    Your access to and use of our game is conditioned on your acceptance of and compliance with these Terms.
    These Terms apply to all visitors, users and others who access or use the game.
    You will need to enter your name and password to have access to our game.
    We can guarantee you that your details will remain confidential and we whatsoever have no right to share it.
    """
    agreement_label = Label(agreement, text=agreement_t, bg="silver")
    agreement_label.pack()

    sound_t ="""This game may have some sound effects or music which may be disturbing to you so we recommend to mute the game
    if you find it difficult to listen.
    """

    sound_label = Label(agreement, text="Sound and Music", bg="silver")
    sound_label['font'] = myFont
    sound_label.pack()
    sound = Label(agreement, text=sound_t, bg="silver")
    sound.pack()



    terms = """
    Please read these Terms and Conditions carefully,
    before playing “Space Invaders ” operated by Guardians of the Galaxy.
    Your access to and use of our game is conditioned on your acceptance of and compliance with these Terms.
    These Terms apply to all visitors, users and others who access or use the game.
    You will need to enter your name and password to have access to our game.
    We can guarantee you that your details will remain confidential and we whatsoever have no right to share it.
    """


    permission_label = Label(agreement, text="Permission", bg="silver")
    permission_label['font'] = myFont
    permission_label.pack()
    permission_t = Label(agreement, text=terms, bg="silver")
    permission_t.pack()
    changes = """
    We reserve the right, at our sole discretion, to modify or replace these Terms at any time.
If any change were to come to our terms that directly or indirectly hampers your data and information,
we will try to provide at least 15 days’ notice prior to any new terms taking effect.
By accessing or using the game, you agree to be bound by these Terms. If you disagree with any part of the terms,
then you may not access the Game."""
    changes_label = Label(agreement, text="Changes and Update", bg="silver")
    changes_label['font'] = myFont
    changes_label.pack()

    changes_t = Label(agreement, text=changes, bg="silver")
    changes_t.pack()

    # inserting check button
    val = StringVar()
    check_button = Checkbutton(agreement, text="Yes, I agree.", bg="teal", font=("Century, Gothic", 22),
                               fg="white", variable=val, onvalue="On", offvalue="Off", command=agree)
    check_button.deselect()
    check_button.pack()



    agreement.mainloop()
