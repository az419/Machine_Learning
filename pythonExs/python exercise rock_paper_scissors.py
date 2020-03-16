"""player1 = str(input("Rock/Paper/Scissors: "))
player2 = str(input("Rock/Paper/Scissors: "))

if(player1 == player2):
    print("Draw")
elif(player1 == "Rock" and player2 == "Paper"):
    print("Player2 is the winner!")
elif(player1 == "Rock" and player2 == "Scissors"):
    print("Player1 is the winner")
elif(player1 == "Paper" and player2 == "Scissors"):
    print("Player2 is the winner")
else:
    print("Error")"""


import random


class RockPaperScissors:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two

    def moves(self):
        return ["Rock", "Scissors", "Paper"]  # list syntax

    def play(self):
        player_one_move = self.player_one.pick_action(self.moves())
        player_two_move = self.player_two.pick_action(self.moves())
        if(player_one_move == player_two_move):
            print("Draw")
        elif(player_one_move == "Rock" and player_two_move == "Paper"):
            print("Random Player wins!")
        elif(player_one_move == "Rock" and player_two_move == "Scissors"):
            print("You win")
        elif(player_one_move == "Paper" and player_two_move == "Scissors"):
            print("Random Player wins")
        else:
            print("Error")


# move_list = []


class HumanPlayer:
    def __init__(self):
        pass

    def pick_action(self, move_list, state=None):
        i = 1

        for move in move_list:
            print(i, ":", move)
            i += 1
        # the list counts start at 0 so we should minus 1
        return move_list[int(input("Please select a move: ")) - 1]
        """else:
            return "Integer is out of range, please enter an integer between 1 to 3"""


class RandomPlayer:
    def pick_action(self, move_list, state=None):
        move = random.choice(move_list)
        print("Random player's move is: ", move)
        return move


H = HumanPlayer()
R = RandomPlayer()
game = RockPaperScissors(H, R)
game.play()
