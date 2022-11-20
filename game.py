import time
from player import Player

player = Player()

class Game:

    def __init__(self) -> None:
        self.choice = player

    def display_title(self):
        print()
        print()
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock.")
        time.sleep(1.3)
        print("A story of friendship, murder, and revenge.")
        time.sleep(1.3)
        print()

    def display_rules(self):
        print()
        print("How to play... ")
        print()
        time.sleep(1.3)
        print("Scissors cuts paper.")
        time.sleep(1.3)
        print("Paper cover Rock.")
        time.sleep(1.3)
        print("Rock crushes Lizard.")
        time.sleep(1.3)
        print("Lizard poisons Spock.")
        time.sleep(1.3)
        print("Spock smashes Scissors.")
        time.sleep(1.3)
        print("Scissors decapitates Lizard.")
        time.sleep(1.3)
        print("Lizard eats paper.")
        time.sleep(1.3)
        print("Paper disproves Spock.")
        time.sleep(1.3)
        print("Spock vaporizes Rock.")
        time.sleep(1.3)
        print("Rock crushes Scissors.")

        print()
        print()

    def numbers_of_players():
        print("How many players? 1, 2 , or 3 to watch a game?")
        player.multiplayer_option()

    def run_game(self):
        pass

    def winner(self):
        pass






