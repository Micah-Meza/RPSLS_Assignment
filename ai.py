from player import Player
import random

class Ai(Player):

    def __init__(self, name):
        super().__init__(name)
        
    def scores(self):
        self.score += 1

    def gesture_pick(self):
        self.player_choice = random.choice(self.gestures)
        print(f"{self.name} picked {self.player_choice}!")
