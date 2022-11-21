from player import Player


class Human(Player):

    def __init__(self, name):
        super().__init__(name)
        # self.name = name
        
        
    def gesture_pick(self, selection):
        if selection == "1":
            print(f"{self.name} picked {self.gesture[0]}!")
        elif selection == "2":
            print(f"{self.name} picked {self.gesture[1]}!")
        elif selection == "3":
            print(f"{self.name} picked {self.gesture[2]}!")
        elif selection == "4":
            print(f"{self.name} picked {self.gesture[3]}!")
        elif selection == "5":
            print(f"{self.name} picked {self.gesture[4]}!")
        else:
            print("Try again.")
            self.gesture(selection = selection)

    def show_list(self):
        for i in Player.gesture:
            print(i)

    def scores(self):
        pass
