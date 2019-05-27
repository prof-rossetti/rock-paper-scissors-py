from game import determine_winner

def test_determination_of_the_winner():
    winner = determine_winner("rock", "paper")
    #winner = determine_winner({"user": "rock", "computer": "paper"})
    assert winner == "THE COMPUTER"
