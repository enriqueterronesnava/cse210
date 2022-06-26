class Jumper:
    """A draw of a man with a parachute.
        The resposaility of the jumper is to draw its diferent stages of the falling

        Attributes:
            _stage (int): The numer of the stage (0-4) 
    """

    def __init__(self):
        """Constructs a new jumper.

        Args:
            self (jumper): An instance of Hider.
        """
        self._stage = 4

    def update_stage(self, stage):
        self._stage = stage

    def get_stage(self):
        return self._stage

    def print_stage(self, stage):
        print()
        if stage == 4:
            print(" ____ ")
            print('/____\\')
            print('\\    /')
            print(' \\  /')
            print('  O ')
            print(' /|\\')
            print(' / \\')
        elif stage == 3:
            print('/____\\')
            print('\\    /')
            print(' \\  /')
            print('  O ')
            print(' /|\\')
            print(' / \\')
        elif stage == 2:
            print('\\    /')
            print(' \\  /')
            print('  O ')
            print(' /|\\')
            print(' / \\')
        elif stage == 1:
            print(' \\  /')
            print('  O ')
            print(' /|\\')
            print(' / \\')
        elif stage == 0:
            print('  X ')
            print(' /|\\')
            print(' / \\')

