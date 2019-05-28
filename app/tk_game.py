
import tkinter
import tkinter.messagebox

from game import *

window = tkinter.Tk()
window.title(GUI_WINDOW_TITLE)

my_message = tkinter.Message(text=WELCOME_MESSAGE, width=1000)

my_select_label = tkinter.Label(text=GUI_PROMPT_MESSAGE)
my_select = tkinter.Listbox()
my_select.insert(1, "rock")
my_select.insert(2, "paper")
my_select.insert(3, "scissors")

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

my_message.pack()
my_select_label.pack()
my_select.pack()
my_button.pack()
window.mainloop()
