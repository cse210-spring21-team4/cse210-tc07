import sys
from game import constants
from asciimatics.widgets import Frame

class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            self (OutputService): An instance of OutputService.
            screen (Screen): An Asciimatics Screen.
        """
        self._screen = screen
        
    def clear_screen(self):
        """Clears the Asciimatics buffer in preparation for the next rendering.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("-" * constants.MAX_X, 0, 0, 7)
        self._screen.print_at("-" * constants.MAX_X, 0, constants.MAX_Y, 7)

    def draw_top(self, player=str, score=int, strikes=int):
        """

        Args:

        """
        strike_text = "X" * strikes
        text = f"{player:<15}Score:{score:<15}{strike_text:>30}"
        self._screen.print_at(text, 0, 20, 7)

    def draw_word(self, words):
        """Renders the given list of words on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            words (list): The actors to render.
        """ 

        text = words.get_words()
        self._screen.print_at(text, words.__get_x(), 20, 7)

    def draw_bottom(self, buffer):
        """

        Args:

        """
        text = buffer.flush_buffer()
        self._screen.print_at(text, 0, 2, 7)

    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        self._screen.refresh()    
