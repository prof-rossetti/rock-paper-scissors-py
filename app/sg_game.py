# credits:
#  + https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/pysimplegui.md
#  + https://pysimplegui.readthedocs.io/en/latest/tutorial/
#  + https://github.com/PySimpleGUI/PySimpleGUI/blob/master/PySimpleGUI.py#L775-L876

import PySimpleGUI as sg

#from game import random_choice, determine_winner, WIN_MESSAGE, LOSE_MESSAGE, TIE_MESSAGE

#sg.Popup("Hello From PySimpleGUI!", "This is the shortest GUI program ever!")

layout = [
    [
        sg.Text("Please choose an option from the dropdown:")
    ],
    [
        #sg.Listbox(values=("rock", "paper", "scissors"), size=(30, 3))
        sg.Listbox(values=("rock", "paper", "scissors"), size=(30, 3), select_mode="single")
    ],
    [
        sg.Submit()
    ]
]

window = sg.Window("My first GUI").Layout(layout)

button, values = window.Read()

#print(values) #> {0: ['scissors']}
#print(values[0]) #> ['scissors']

print("USER SELECTION:", values[0][0])
