import time
from player import Player
from ai import Ai
from human import Human



class Game:

    def __init__(self) -> None:
        pass

    def display_title(self):
        print()
        print()
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock.")
        # time.sleep(1.3)
        print("A story of friendship, murder, and revenge.")
        # time.sleep(1.3)
        print()

    def display_rules(self):
        print("Use the numnber keys to enter your selection.")
        print("Winner will be best of three. ")
        print()   
        
    def display_instructions(self):
        print()
        print("How to play... ")
        print()
        # time.sleep(1.3)
        print("Scissors cuts paper.")
        # time.sleep(1.3)
        print("Paper cover Rock.")
        # time.sleep(1.3)
        print("Rock crushes Lizard.")
        # time.sleep(1.3)
        print("Lizard poisons Spock.")
        # time.sleep(1.3)
        print("Spock smashes Scissors.")
        # time.sleep(1.3)
        print("Scissors decapitates Lizard.")
        # time.sleep(1.3)
        print("Lizard eats paper.")
        # time.sleep(1.3)
        print("Paper disproves Spock.")
        # time.sleep(1.3)
        print("Spock vaporizes Rock.")
        # time.sleep(1.3)
        print("Rock crushes Scissors.")

        print()
        print()

    def multiplayer_option(self):
        print("How many players?\n1. Player vs Ai,\n2 Human vs Human,\n3 Ai vs Ai?")
        print()
        option = input("What is your choice? ")
        if option == "1":
            print("Player vs Ai")
            print()
            print("Starting ...")
            print()
            human_player_1 = Human("Player 1")
            ai_player_1 = Ai("Ai")
            player = Player()
            

        elif option == "2":
            print("Player vs Player")
            print()
            print("Starting ...")
            print()
            human_player_1 = Human("Player 1")
            human_player_2 = Human("Player 2")
            player = Player()
            

        elif option == "3":
            print("Ai vs Ai")
            print()
            print("Starting ...")
            print()
            ai_player_1 = Ai("Ai 1")
            ai_player_2 = Ai("Ai 2")
            player = Player()
            

        else:
            print("Try again.")
            print()
            self.multiplayer_option()

    def run_game(self):
        cont = True
        self.display_title()
        self.display_instructions()
        self.display_rules()
        self.multiplayer_option()
        
        while cont != False:
            pass



    def winner(self):
        pass






