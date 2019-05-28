
import PySimpleGUI as sg

from game import *

layout = [
    [ sg.Text(GUI_PROMPT_MESSAGE) ],
    [ sg.Listbox(values=("rock", "paper", "scissors"), size=(30, 3), select_mode="single") ],
    [ sg.Submit() ]
]


window = sg.Window(GUI_WINDOW_TITLE).Layout(layout)

button, values = window.Read()

user_choice = values[0][0] #> "scissors"
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

sg.Popup("Results...", message)
