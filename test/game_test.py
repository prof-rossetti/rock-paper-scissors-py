from app.game import random_choice, determine_winner

def test_random_choice():
    assert random_choice() in ["rock", "paper", "scissors"]

    custom_options = [1, 5, 7]
    assert random_choice(custom_options) in custom_options

def test_determination_of_the_winner():
    assert determine_winner("rock", "rock") == None
    assert determine_winner("rock", "paper") == "paper"
    assert determine_winner("rock", "scissors") == "rock"

    assert determine_winner("paper", "rock") == "paper"
    assert determine_winner("paper", "paper") == None
    assert determine_winner("paper", "scissors") == "scissors"

    assert determine_winner("scissors", "rock") == "rock"
    assert determine_winner("scissors", "paper") == "scissors"
    assert determine_winner("scissors", "scissors") == None
