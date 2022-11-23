from player import Player
import maskpass # To mask the Human vs Human option.

class Human(Player):

    def __init__(self, name):
        super().__init__(name)
        # self.name = name
        
        
    def gesture_pick(self):
        self.show_list()
        print()
        selection = input("Enter your choice. ")
        print()

        if selection == "0":
            self.player_choice = self.gestures[0]
            print(f"{self.name} picked {self.player_choice}!")
        elif selection == "1":
            self.player_choice = self.gestures[1]
            print(f"{self.name} picked {self.player_choice}!")
        elif selection == "2":
            self.player_choice = self.gestures[2]
            print(f"{self.name} picked {self.player_choice}!")
        elif selection == "3":
            self.player_choice = self.gestures[3]
            print(f"{self.name} picked {self.player_choice}!")
        elif selection == "4":
            self.player_choice = self.gestures[4]
            print(f"{self.name} picked {self.player_choice}!")
        else:
            print("Try again.")
            self.gesture_pick()

    # This is for the Human vs Human each player cannot see what the other put in. 
    def gesture_pick_2(self):
        self.show_list()
        print()
        selection = maskpass.askpass(f"{self.name} make your choice: ") # To mask the player input on player vs player.
        # selection = input("Enter your choice. ") # incase if the maskpass import does work.
        print()

        if selection == "0":
            self.player_choice = self.gestures[0]       
        elif selection == "1":
            self.player_choice = self.gestures[1]           
        elif selection == "2":
            self.player_choice = self.gestures[2]           
        elif selection == "3":
            self.player_choice = self.gestures[3]
        elif selection == "4":
            self.player_choice = self.gestures[4]
        else:
            print("Try again.")
            self.gesture_pick_2()

    def show_list(self):
        index = 0
        for i in self.gestures:
            print(f"{index}.) : {i}")
            index += 1

    def scores(self):
        self.score += 1
