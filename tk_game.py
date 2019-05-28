# adapted from notes: https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/tkinter.md

import tkinter

window = tkinter.Tk()

my_message = tkinter.Message(text="Hi. Welcome to my Rock-Paper-Scissors game!", width=1000)

my_select_label = tkinter.Label(text="Please choose an option from the dropdown:")
my_select = tkinter.Listbox()
my_select.insert(1, "rock")
my_select.insert(2, "paper")
my_select.insert(3, "scissors")

def handle_button_click():
    print("------------------------------")
    print("You chose:", my_select.get(my_select.curselection()))

my_button = tkinter.Button(text="Click Me", command=handle_button_click)

my_select.pack()
my_button.pack()
window.mainloop()
