import random

class Player:

    #  Sets the starting score for both players

    score = 0

    def __init__(self):

        self.my_move = None

        self.their_move = None

    #  Stores players moves

    def learn(self, my_move, their_move):

        self.my_move = my_move

        self.their_move = their_move

class HumanPlayer(Player):

    def __init__(self):

        super().__init__()

        self.behavior = 'Human Player'

    def move(self):

        while True:

            #  Gets the user input from moves list options

            move = input(

                'CHOOSE A MOVE: (rock / paper / scissors / '

                'lizard / spock)\n').lower()

            #  Validates if the user input is on the moves list

            if move in moves:

                return move

            else:

                print('The name of the move is wrong. Try again!')

class RandomPlayer(Player):

    def move(self):

        #  Return any of the options inside moves list randomly

        return random.choice(moves)

class RepeatPlayer(Player):

    def move(self):

        #  Always plays rock

        return 'rock'

class ReflectPlayer(Player):

    def move(self):

        #  Plays randomly if the other player has not moved

        if self.their_move is None:

            return random.choice(moves)

        else:

            #  Returns the same as the other player

            return self.their_move

class CyclePlayer(Player):

    def move(self):

        if self.my_move is None:

            return random.choice(moves)

        else:

            index = moves.index(self.my_move) + 1

            if index == len(moves):

                index = 0

            return moves[index]

def p1_win(one, two):

    #  Sets the win options for player 1

    return ((one == 'scissors' and two == 'paper') or

            (one == 'paper' and two == 'rock') or

            (one == 'rock' and two == 'lizard') or

            (one == 'lizard' and two == 'spock') or

            (one == 'spock' and two == 'scissors') or

            (one == 'scissors' and two == 'lizard') or

            (one == 'lizard' and two == 'paper') or

            (one == 'paper' and two == 'spock') or

            (one == 'spock' and two == 'rock') or

            (one == 'rock' and two == 'scissors'))

def p2_win(one, two):

    #  Sets the win options for player 2

    return ((one == 'paper' and two == 'scissors') or

            (one == 'rock' and two == 'paper') or

            (one == 'lizard' and two == 'rock') or

            (one == 'spock' and two == 'lizard') or

            (one == 'scissors' and two == 'spock') or

            (one == 'lizard' and two == 'scissors') or

            (one == 'paper' and two == 'lizard') or

            (one == 'spock' and two == 'paper') or

            (one == 'rock' and two == 'spock') or

            (one == 'scissors' and two == 'rock'))

class Game:

    def __init__(self, player1, player2):

        #  Defines two players which are going to play the gane

        self.player1 = player1

        self.player2 = player2

    def play_round(self):

        move1 = self.player1.move()

        move2 = self.player2.move()

        #  Prints each player nove

        print(f'Player 1: {move1}  Player 2: {move2}')

        #  Player 1 wins

        if p1_win(move1, move2) is True and p2_win(move1, move2) is False:

            #  Adds one more point each time the player wins

            self.player1.score += 1

            print('-- YOU WIN! --\n')

        #  Player 2 wins

        elif p2_win(move1, move2) is True and p1_win(move1, move2) is False:

            #  Adds one more point each time the player wins

            self.player2.score += 1

            print('-- F**K! --\n')

        #  Tie

        else:

            print("-- IT'S A TIE --\n")

        self.player1.learn(move1, move2)

        self.player2.learn(move2, move1)

        print('       SCORE')

        #  Prints the result for each round and

        print(

            f'Human: {self.player1.score} | Computer: {self.player2.score}\n')

    def play_game(self):

        print('Game starts!\n')

        # Each game is composed of 3 rounds

        for round in range(3):

            print(f'Round {round}:')

            self.play_round()

        print('Game over!\n\n')

        #  When the game ends reset the global score to 0 again

        self.player1.score = 0

        self.player2.score = 0

if __name__ == '__main__':

    moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    behaviors = {

        'human': HumanPlayer(),

        'reflect': ReflectPlayer(),

        'cycle': CyclePlayer(),

        'random': RandomPlayer(),

        'repeat': RepeatPlayer()

    }

    while True:

        print('ROCK, PAPER, SCISSORS, LIZARD, SPOCK - GO!\n')

        print(

            'Here are the rules of the game: \nScissors cuts paper. '

            'Paper covers rock. Rock crushes lizard. Lizard poisons Spock. '

            'Spock smashes scissors. Scissors decapitates lizard. Lizard '

            'eats paper. Paper disproves Spock. Spock vaporizes rock and '

            'as it always has, rock crushes scissors.\n')

        #  Gets the user input from behaviors list options

        choice = input(

            'CHOOSE AN OPPONENT: (random / reflect / repeat'

            ' / cycle)\n').lower()

        # If player choose a correct opponent the game starts between the

        #  human player and the chosen opponent

        if choice in behaviors:

            game = Game(behaviors['human'], behaviors[choice])

            game.play_game()

        else:

            print('Wrong player. Try again!')
