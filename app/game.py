
import random

GUI_WINDOW_TITLE = "Rock-Paper-Scissors"
WELCOME_MESSAGE = "Hi. Welcome to my Rock-Paper-Scissors game!"
GUI_PROMPT_MESSAGE = "Please choose an option from the dropdown:"

WIN_MESSAGE = "Congratulations, you won!"
LOSE_MESSAGE = "Oh, the computer won. It's ok."
TIE_MESSAGE = "Oh, it's a tie."

def random_choice(options=["rock", "paper", "scissors"]):
    return random.choice(options)

def determine_winner(choice1, choice2):
    """
    Determines the winning choice between two choices from selectable options: "rock", "paper", or "scissors".
    Returns the winning choice (e.g. "paper"), or None if there is a tie.
    Example: determine_winner("rock", "paper")
    """

    #if choice1 == choice2:
    #    winner = None # the outcome is a tie
    #else:
    #    choices = [choice1, choice2]
    #    choices.sort() # FYI: this is mutating
#
    #    if choices == ["paper", "rock"]:
    #        winner = "paper"
    #    elif choices == ["paper", "scissors"]:
    #        winner = "scissors"
    #    elif choices == ["rock", "scissors"]:
    #        winner = "rock"
    #    else:
    #        raise ValueError("OOPS, SOMETHING WENT WRONG")

    winners = {
        "rock":{
            "rock": None, # represents a tie
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None, # represents a tie
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None, # represents a tie
        },
    }

    # todo: handle keyerror
    winner = winners[choice1][choice2]

    return winner

if __name__ == "__main__":

    print("-------------------")
    print("Launching the game...")
    print("-------------------")

    options = ["rock", "paper", "scissors"]

    user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

    if user_choice in options:
        print("You chose:", user_choice)
    else:
        print("Expecting one of: 'rock', 'paper', or 'scissors' (lower case, without the quotation marks). Please try again.")
        exit()

    computer_choice = random_choice(options)
    print("The computer chose:", computer_choice)
    print("-------------------")

    winning_choice = determine_winner(user_choice, computer_choice)

    if winning_choice:
        if winning_choice == user_choice:
            print(WIN_MESSAGE)
        elif winning_choice == computer_choice:
            print(LOSE_MESSAGE)
    else:
        print(TIE_MESSAGE)

    print("Thanks for playing. Please play again!")
