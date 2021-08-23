from tkinter import *
from tkinter.font import *

agreement = Tk()
agreement.title("Terms and Conditions")
agreement.geometry("900x800")
agreement.iconbitmap("agree_0.ico")

# using different fonts for different headings
myFont = Font(size=20, weight="bold")

# adding background image and including all buttons and labels inside the frame
bg_photo = PhotoImage(file="agree_1.png")
window_frame = Label(agreement, image=bg_photo)
window_frame.place(x=0, y=0, relwidth=1, relheight=1)



# function for agree
def agree():
    response = val.get()
    if response == "On":
        continue_button = Button(window_frame, text="Continue", highlightbackground="yellow",
                                 font=("Century, Gothic", 20), padx=9, pady=9)  # #FFFF00 = yellow color
        continue_button.grid(row=11, column=0)
    else:
        continue_button = Button(window_frame, text="Continue", bg="#FFFF00", font=("Century, Gothic", 20),
                                 state=DISABLED, padx=9, pady=9)  # #FFFF00 = yellow color
        continue_button.grid(row=11, column=0)

# files handling and labelling
terms_and_condition_label = Label(window_frame, text="Terms and Conditions")
terms_and_condition_label['font'] = myFont
terms_and_condition_label.grid(row=0, column=0)

with open('terms_and_conditions.txt', encoding='utf8') as f:
    lines = f.read()
terms_label = Label(window_frame, text=lines)
terms_label.grid(row=1, column=0)

#lines.split("######")

sound_label = Label(window_frame, text="Sound and music")
sound_label['font'] = myFont
sound_label.grid(row=2, column=0)

with open('sound_music.txt', 'r') as f:
    lines = f.read()
terms_label = Label(window_frame, text=lines)
terms_label.grid(row=3, column=0)

permission_label = Label(window_frame, text="Permission")
permission_label['font'] = myFont
permission_label.grid(row=4, column=0)

with open('permission.txt', encoding='utf8') as f:
    lines = f.read()
permission_label = Label(window_frame, text=lines)
permission_label.grid(row=5, column=0)

changes_label = Label(window_frame, text="Changes and Update")
changes_label['font'] = myFont
changes_label.grid(row=6, column=0)
changes_label = Label(window_frame, text="Changes and Update")
changes_label['font'] = myFont
changes_label.grid(row=12, column=0)
changes_label = Label(window_frame, text="Changes and Update")
changes_label['font'] = myFont
changes_label.grid(row=15, column=0)
with open('changes.txt', 'r') as f:
    lines = f.readlines()
changes_label = Label(window_frame, text=lines)
changes_label.grid(row=7, column=0)

empty_label = Label(window_frame, text="")
empty_label.grid(row=8, column=0)
empty_label = Label(window_frame, text="")
empty_label.grid(row=10, column=0)
# inserting check button
val = StringVar()
check_button = Checkbutton(window_frame, text="Yes, I agree.", bg="blue", font=("Century, Gothic", 22),
                           fg="white", variable=val, onvalue="On", offvalue="Off", command=agree)
check_button.deselect()
check_button.grid(row=9, column=0)

continue_button = Button(window_frame, text="Continue", font=("Century, Gothic", 20),
                         state=DISABLED, padx=9, pady=9)  #  #FFFF00 = yellow color
continue_button.grid(row=11, column=0)

agreement.mainloop()
