# adapted from notes: https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/pysimplegui.md

import PySimpleGUI as sg

#from game import random_choice, determine_winner, WIN_MESSAGE, LOSE_MESSAGE, TIE_MESSAGE




#sg.Popup("Hello From PySimpleGUI!", "This is the shortest GUI program ever!")


layout = [
    [sg.Text("Enter your name"), sg.InputText()],
    [sg.OK()]
]

window = sg.Window("My first GUI").Layout(layout)

# button, (name,) = window.Read()
# print("NAME:", name) # name is zero

#breakpoint()

# type(window) #> <class 'PySimpleGUI.PySimpleGUI.Window'>

button, values = window.Read()

#print("BUTTON:", button) #> "OK"
#print(type(values)) #> dict
#print("VALUES:", values) #> VALUES: {0: 'Polly Professor'}

print("NAME:", values[0])
