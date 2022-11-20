from human import Human
from ai import Ai

class Player:

    def __init__(self):
        self.name = "Blue"
        

    def gesture(self):
        pass

    def score(self):
        pass

    def multiplayer_option(self):
        print()
        option = input("What is your choice? ")
        if option == "1":
            print("Player vs Ai")
            print()
            human_player_1 = Human("Player 1")
            ai_player_1 = Ai("Ai")
        elif option == "2":
            print("Player vs Player")
            print()
            human_player_1 = Human("Player 1")
            human_player_2 = Human("Player 2")
        elif option == "3":
            print("Ai vs Ai")
            print()
            ai_player_1 = Ai("Ai 1")
            ai_player_2 = Ai("Ai 2")

        else:
            print("Try again.")
            print()
            self.multiplayer_option()


