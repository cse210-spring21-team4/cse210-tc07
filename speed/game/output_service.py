from game import constants


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

    def draw_top(self, player=str, score=int, strikes=int):
        """Draws the top of the game screen to show the player name,
        score, and strikes of the current game.

        Args:
            self (OuputService): an instance of OutputService.
        """
        strike_text = "X" * strikes
        text = f"{player:<15}Score:{score:<15}{strike_text:>30}"
        self._screen.print_at(text, 0, 20, 7)

    def draw_word(self, words: dict):
        """Renders the given dictionary of words on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            words (dictionary): The actors to render.
        """

        for word in words.items():
            text = word[0]
            x, y = word[1]
            self._screen.print_at(text, x, y, 7)

    def draw_bottom(self, buffer=str):
        """

        Args:

        """
        text = buffer
        self._screen.print_at(text, 0, 2, 7)

    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """
        self._screen.refresh()
