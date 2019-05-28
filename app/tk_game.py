import os
from tkinter import * # provides Label
#import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk

from game import *

window = tkinter.Tk()
window.title(GUI_WINDOW_TITLE)

img_filepath = os.path.join(os.path.dirname(__file__), "..", "img", "rps_winners.jpg")
window.tk.call("wm", "iconphoto", window._w, ImageTk.PhotoImage(file=img_filepath)) # h/t https://stackoverflow.com/a/31816987/670433

header = Label(window)
header_img_filepath = os.path.join(os.path.dirname(__file__), "..", "img", "rps_options.jpg")
img = Image.open(header_img_filepath)
header.img = ImageTk.PhotoImage(img)
header['image'] = header.img
header.pack()

my_message = tkinter.Message(text=WELCOME_MESSAGE, width=1000)
my_message.pack()

my_select_label = tkinter.Label(text=GUI_PROMPT_MESSAGE)
my_select_label.pack()

my_select = tkinter.Listbox()
my_select.insert(1, "rock")
my_select.insert(2, "paper")
my_select.insert(3, "scissors")
my_select.pack()

def handle_button_click():

    user_choice = my_select.get(my_select.curselection())
    computer_choice = random_choice()
    winning_choice = determine_winner(user_choice, computer_choice)

    message = "-------------------"
    message += f"\nYou chose: {user_choice}"
    message += f"\nThe computer chose: {computer_choice}"
    message += "\n-------------------"

    if winning_choice:
        if winning_choice == user_choice:
            message += f"\n{WIN_MESSAGE}"
        elif winning_choice == computer_choice:
            message += f"\n{LOSE_MESSAGE}"
    else:
        message += f"\n{TIE_MESSAGE}"

    message += "\n-------------------"
    message += "\nThanks for playing. Please play again!"

    tkinter.messagebox.showinfo("Results...", message)

my_button = tkinter.Button(text="Submit", command=handle_button_click)
my_button.pack()

window.mainloop()
