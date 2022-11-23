import time
from player import Player
from ai import Ai
from human import Human


class Game:

    def __init__(self) -> None:
        self.player_1 = Human("")
        self.player_2 = Human("")
 
        
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
        print("Scissors cuts Paper.")
        # time.sleep(1.3)
        print("Paper covers Rock.")
        # time.sleep(1.3)
        print("Rock crushes Lizard.")
        # time.sleep(1.3)
        print("Lizard poisons Spock.")
        # time.sleep(1.3)
        print("Spock smashes Scissors.")
        # time.sleep(1.3)
        print("Scissors decapitates Lizard.")
        # time.sleep(1.3)
        print("Lizard eats Paper.")
        # time.sleep(1.3)
        print("Paper disproves Spock.")
        # time.sleep(1.3)
        print("Spock vaporizes Rock.")
        # time.sleep(1.3)
        print("Rock crushes Scissors.")
        # time.sleep(1.3)
        print()
        print()

        
    def multiplayer_option(self):
        print()
        print("How many players?\n1. Player vs Ai\n2. Human vs Human\n3. Ai vs Ai ")
        print()
        option = input("What is your choice? ")
        if option == "1":
            print("Player vs Ai")
            print()
            print("Starting ...")
            print()
            self.player_1 = Human("Player 1")
            self.player_2 = Ai("Ai")
                      

        elif option == "2":
            print("Player vs Player")
            print()
            print("Starting ...")
            print()
            self.player_1 = Human("Player 1")
            self.player_2 = Human("Player 2")
            return option
            
            

        elif option == "3":
            print("Ai vs Ai")
            print()
            print("Starting ...")
            print()
            self.player_1 = Ai("Ai 1")
            self.player_2 = Ai("Ai 2")
                

        else:
            print("Try again.")
            print()
            self.multiplayer_option()

            
    def run_game(self):
        cont = True
        
        self.display_title()
        self.display_instructions()
        self.display_rules()
        while cont == True:
            cont_2 = True
            option = self.multiplayer_option()
            if option == "2":
                self.alt_round()
            else:
                self.round()

            while cont_2 == True: 
                stop = input("Would you like to play again? (Y/N) -> ")
            
                if stop == "Y" or stop == "y":
                    cont = True
                    cont_2 = False
                elif stop == "N" or stop == "n":
                    cont = False
                    cont_2 =False
                else: 
                    print("Try again. ")
        

    def round(self):
        cont = True
        while cont == True:
            self.player_1.gesture_pick()
            self.player_2.gesture_pick()
            self.round_winner()
            if self.player_1.score == 2 or self.player_2.score == 2:
                self.game_winner()
                cont = False
            else:
                cont = True
    
                
    def alt_round(self):
        cont = True
        while cont == True:
            self.player_1.gesture_pick_2()
            self.player_2.gesture_pick_2()
            self.round_winner()
            if self.player_1.score == 2 or self.player_2.score == 2:
                self.game_winner()
                cont = False
            else:
                cont = True

        
    def round_winner(self):
        if self.player_1.player_choice == self.player_2.player_choice and self.player_2.player_choice == self.player_1.player_choice:
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice} is a tie. Go again! ")
            print()

        elif self.player_1.player_choice == 'Rock' and self.player_2.player_choice == 'Scissors':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_1.name} wins the round! ")
            self.player_1.scores() 
            print()
            print()
            
        elif self.player_1.player_choice == 'Scissors' and self.player_2.player_choice == 'Rock':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_2.name} wins the round! ")
            self.player_2.scores() 
            print()
            print()
        
        elif self.player_1.player_choice == 'Scissors' and self.player_2.player_choice == 'Paper':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_1.name} wins the round! ")
            self.player_1.scores() 
            print()
            print()
            
        elif self.player_1.player_choice == 'Paper' and self.player_2.player_choice == 'Scissors':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_2.name} wins the round! ")
            self.player_2.scores() 
            print()
            print()

        elif self.player_1.player_choice == 'Paper' and self.player_2.player_choice == 'Rock':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_1.name} wins the round! ")
            self.player_1.scores() 
            print()
            print()
            
        elif self.player_1.player_choice == 'Rock' and self.player_2.player_choice == 'Paper':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_2.name} wins the round! ")
            self.player_2.scores() 
            print()
            print()

        elif self.player_1.player_choice == 'Rock' and self.player_2.player_choice == 'Lizard':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_1.name} wins the round! ")
            self.player_1.scores() 
            print()
            print()
            
        elif self.player_1.player_choice == 'Lizard' and self.player_2.player_choice == 'Rock':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_2.name} wins the round! ")
            self.player_2.scores() 
            print()
            print()

        elif self.player_1.player_choice == 'Lizard' and self.player_2.player_choice == 'Spock':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_1.name} wins the round! ")
            self.player_1.scores() 
            print()
            print()
            
        elif self.player_1.player_choice == 'Spock' and self.player_2.player_choice == 'Lizard':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_2.name} wins the round! ")
            self.player_2.scores() 
            print()
            print()
            
        elif self.player_1.player_choice == 'Spock' and self.player_2.player_choice == 'Scissors':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_1.name} wins the round! ")
            self.player_1.scores() 
            print()
            print()
            
        elif self.player_1.player_choice == 'Scissors' and self.player_2.player_choice == 'Spock':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_2.name} wins the round! ")
            self.player_2.scores() 
            print()
            print()

        elif self.player_1.player_choice == 'Scissors' and self.player_2.player_choice == 'Lizard':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_1.name} wins the round! ")
            self.player_1.scores() 
            print()
            print()
            
        elif self.player_1.player_choice == 'Lizard' and self.player_2.player_choice == 'Scissors':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_2.name} wins the round! ")
            self.player_2.scores() 
            print()
            print()

        elif self.player_1.player_choice == 'Lizard' and self.player_2.player_choice == 'Paper':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_1.name} wins the round! ")
            self.player_1.scores() 
            print()
            print()
            
        elif self.player_1.player_choice == 'Paper' and self.player_2.player_choice == 'Lizard':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_2.name} wins the round! ")
            self.player_2.scores() 
            print()
            print()

        elif self.player_1.player_choice == 'Paper' and self.player_2.player_choice == 'Spock':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_1.name} wins the round! ")
            self.player_1.scores() 
            print()
            print()
            
        elif self.player_1.player_choice == 'Spock' and self.player_2.player_choice == 'Paper':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_2.name} wins the round! ")
            self.player_2.scores() 
            print()
            print()
            
        elif self.player_1.player_choice == 'Spock' and self.player_2.player_choice == 'Rock':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_1.name} wins the round! ")
            self.player_1.scores() 
            print()
            print()
            
        elif self.player_1.player_choice == 'Rock' and self.player_2.player_choice == 'Spock':
            print(f"{self.player_1.player_choice} and {self.player_2.player_choice}. {self.player_2.name} wins the round! ")
            self.player_2.scores() 
            print()
            print()

            
    def game_winner(self):
        if self.player_1.score == 2:
            print(f"{self.player_1.name} has {self.player_1.score} and wins best of three. ")
            print()
        else:
            print(f"{self.player_2.name} has {self.player_2.score} and wins best of three. ")
            print()





