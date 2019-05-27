from game import determine_winner

def test_determination_of_the_winner():
    #assert determine_winner("rock", "rock") == None
    #assert determine_winner("rock", "paper") == "paper"
    assert determine_winner("rock", "scissors") == "rock"
