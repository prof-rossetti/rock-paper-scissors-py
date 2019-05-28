# adapted from notes: https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/tkinter.md

import random

import tkinter
import tkinter.messagebox # h/t: https://stackoverflow.com/a/38181986/670433

from game import determine_winner

window = tkinter.Tk()

my_message = tkinter.Message(text="Hi. Welcome to my Rock-Paper-Scissors game!", width=1000)

my_select_label = tkinter.Label(text="Please choose an option from the dropdown:")
my_select = tkinter.Listbox()
my_select.insert(1, "rock")
my_select.insert(2, "paper")
my_select.insert(3, "scissors")

def handle_button_click():
    user_choice = my_select.get(my_select.curselection())
    print("------------------------------")
    print("You chose:", user_choice)

    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    print("------------------------------")
    print("The computer chose:", computer_choice)


    result_message = f"You chose: {user_choice} \n"
    result_message += f"The computer chose: {computer_choice} \n"

    #winning_choice = determine_winner(user_choice, computer_choice)
    result_message += "You won!"

    tkinter.messagebox.showinfo("Congratulations", result_message)

my_button = tkinter.Button(text="Submit", command=handle_button_click)

my_select.pack()
my_button.pack()
window.mainloop()
