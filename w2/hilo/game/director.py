from game.card import card

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    
    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 300
        self.total_score = 0
    
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            card_value = card.reveal(self)
            print(f"The card is: {card_value}")
            new_card = card.reveal(self)
            HoL = ""
            while new_card != card_value:
                if new_card > card_value:
                    HoL = "h"
                    break
                elif new_card < card_value:
                    HoL = "l"
                    break
                else:
                    new_card = card.reveal()

            player_answer = self.get_inputs()
            print(f"The next card was: {new_card}")
            if player_answer == HoL:
                self.score += 100
            else:
                self.score -= 75    

            print(f"Your score is: {self.score}")  
            self.continue_g()  
            print()
            if self.score <= 0:
                self.is_playing = False
            
            

        print("Game over")    

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        response = input("Higher or lower? [h/l] ")
        return response

    def continue_g(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        play = input("Play again? [y/n] ")
        self.is_playing = (play == "y")
