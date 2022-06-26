import random
from game.jumper import Jumper
class WBank:
    """A Word bank that have words inside.
        The responsability of the word bank is to give words to the board
        Args:
            _words (List[int]): A list of words to display
    """
    def __init__(self):
        self._wordsl = ["pillow", "coffee", "bed", "spoon", "blanket", "knife", "stove", "sink",
        "machine" "pot", "dish", "fridge", "sofa", "stool", "cup", "fork", "glass"]

        self._word =  list(self._wordsl[random.randint(0, self._wordsl.__len__()-1)])
        self._user_word = []
        self._jumper = Jumper()

    def print_board(self):
        word = self._word
        uword = self._user_word
        board = ""
        for i in word:
            if i in uword:
                board += i + " "
            else:
                board += "_ "

        print(board)


    def check_letter(self, uword, word, letter, count):
        while True:
            if letter in uword:
                print("That letter is already guessed")
                break
            else:
                uword.append(letter)
                if letter in word:
                    break
                else:
                    count -= 1  
                    self._jumper.update_stage(count)
                    break
                    



