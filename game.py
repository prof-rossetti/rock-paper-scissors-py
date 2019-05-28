
import random

def determine_winner(choice1, choice2):
    """
    Determines the winning choice between two choices from selectable options: "rock", "paper", or "scissors".
    Returns the winning choice (e.g. "paper"), or None if there is a tie.
    Example: determine_winner("rock", "paper")
    """

    if choice1 == choice2:
        winner = None # the outcome is a tie
    else:
        choices = [choice1, choice2]
        choices.sort() # FYI: this is mutating

        if choices == ["paper", "rock"]:
            winner = "paper"
        elif choices == ["paper", "scissors"]:
            winner = "scissors"
        elif choices == ["rock", "scissors"]:
            winner = "rock"
        else:
            raise ValueError("OOPS, SOMETHING WENT WRONG")

    return winner


if __name__ == "__main__":

    #
    # CAPTURE INPUTS
    #

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

    computer_choice = random.choice(options)
    print("The computer chose:", computer_choice)
    print("-------------------")

    #
    # PROCESS INPUTS INTO OUTPUTS
    #

    winning_choice = determine_winner(user_choice, computer_choice)

    #
    # DISPLAY OUTPUTS
    #

    if winning_choice:
        if winning_choice == user_choice:
            print("Congratulations, you won!")
        elif winning_choice == computer_choice:
            print("Oh, the computer won. It's ok.")
    else:
        print("Oh, it's a tie.")

    print("Thanks for playing. Please play again!")
