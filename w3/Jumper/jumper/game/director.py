from game.wbank import WBank
from game.terminal_service import TerminalService
from game.jumper import Jumper

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._wbank = WBank()
        self._tservice = TerminalService()
        self._jumper = Jumper()
        self._is_playing = True
        self._user_letter = ""
        self._count = 4
        
    
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        print()
        print("Welcome to the Jumper game!")
        self._wbank.print_board()
        self._jumper.print_stage(self._count)

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
    
        print("GAME OVER, THANKS FOR PLAYING")
        print()
    def _get_inputs(self):
        self._user_letter = self._tservice.read_text("\nGuess a letter [a-z]: ")

    def _do_updates(self):
        self._wbank.check_letter(self._wbank._user_word, self._wbank._word, self._user_letter, self._wbank._jumper._stage)
        newstafe = self._wbank._jumper._stage
        if newstafe <= 0:
            self._is_playing = False

        
    def _do_outputs(self):
        self._wbank.print_board()
        self._jumper.print_stage(self._wbank._jumper._stage)
        
    
