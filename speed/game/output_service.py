from game import constants
from asciimatics.widgets import Frame


class Output_Service:
    """Outputs the game state. The responsibility of the class of objects is to
    draw the game state on the terminal.

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

    def draw_top(self, player: str, level: int, score: int, strikes: int):
        """Draws the top of the game screen to show the player name,
        score, and strikes of the current game.

        Args:
            self (OuputService): an instance of OutputService.
            player (string): name(s) of player(s) to render
            score (int): score of game to render
            strikes (int): strikes of game to render
        """
        strike_text = "X" * strikes
        level_text = f"Lvl. {level}"
        score_text = f"Score: {score}"
        text = f"{player:<15}{level_text:<15}{score_text:>15}{strike_text:>15}"
        self._screen.print_at(text, 0, 20, 7)

    def draw_word(self, words: dict):
        """Renders the given dictionary of words on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            words (dictionary): The words to render.
        """ 
        for word in words.items():
            text = word[0]
            x, y = word[1]
            self._screen.print_at(text, x, y, 7)

    def draw_bottom(self, buffer=str):
        """Renders the buffer of the game to keep track of the input from 
        the user.

        Args:
            self (OuputService): An instance of OuputService.
            buffer (string): The buffer to render
        """
        text = buffer
        self._screen.print_at(text, 0, 2, 7)

    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """
        self._screen.refresh()
