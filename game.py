
import random

def determine_winner(choice1, choice2):
    """
    Determines the winning choice between two choices from selectable options: "rock", "paper", or "scissors".
    Returns the winning choice, or None if there is a tie.
    Example: determine_winner("rock", "paper")
    """
    return "rock"

if __name__ == "__main__":

    print("-------------------")
    print("LAUNCHING THE GAME...")
    print("-------------------")

    options = ["rock", "paper", "scissors"]

    user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

    if user_choice in options:
        print("YOU CHOSE:", user_choice.upper())
    else:
        error_message = "Expecting one of: 'rock', 'paper', or 'scissors' (lower case, without the quotation marks). Please try again."
        #raise ValueError(error_message)
        print(error_message)
        exit()

    computer_choice = random.choice(options)
    print("THE COMPUTER CHOSE:", computer_choice.upper())

    winner = determine_winner(user_choice, computer_choice)
    print("-------------------")
    print(f"{winner} IS THE WINNER!")
    print("THANKS FOR PLAYING. PLEASE PLAY AGAIN!")
