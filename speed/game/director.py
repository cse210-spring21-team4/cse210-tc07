
from time import sleep
from game import constants
from game.words import Words
from game.scoreboard import Scoreboard
from game.buffer import Buffer
# AGNES check import names with GitHub.

class Director:
    """A code template for a person who directs the game.
    The responsibility of this class of objects is to control
    the sequence of one round of play.

    Stereotype:
        Controller

    Attributes:
        words (Words): The player's target is to type the falling words.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        scoreboard (Scoreboard): The current score.
        buffer (Buffer): The player types the word.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        # (AH) Class attributes.
        self._words = Words()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._scoreboard = Scoreboard()
        self._buffer = Buffer()

    def start_game(self, player):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        # (AH) changed from 'input' to print.
        print(f'Game started. Player is {player}')

        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play.
        In this case,
        that means getting the words typed by the player.

        Args:
            self (Director): An instance of Director.
        """

        # AGNES check with Sarah's code.
        letter = self.input_service.get_letter()
        self._buffer.update_buffer(letter)

    def _do_updates(self):
        """Updates the important game information for each round of play.
        In this case, that means checking that word typed by player
        in Buffer is the same as the random word from the word list.

        Args:
            self (Director): An instance of Director.
        """

