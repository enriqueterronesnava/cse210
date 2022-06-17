import random

class card:
    """Small rectangular-shaped cardboard that has a figure or a certain number of objects 
    printed on one of its faces and a uniform drawing on the other; 
    together with others, it forms the deck..

    The responsibility of card is to keep track of the side facing up.

    Attributes:
        value (int): The number of spots on the side facing up.
    """
    def __init__(self):
        """Constructs a new instance of a card.

        Args:
            self (card): An instance of a card.
        """
        self.value = 0

    def reveal(self):
        """Generates a new random value and calculates the points for the card.
        
        Args:
            self (card): An instance of a card.
        """
        self.value = random.randint(1, 13)
        return self.value
        