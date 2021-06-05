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
        # (AH) see get_inputs().
        self.letter = None

    def start_game(self, player):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        # (AH) changed from 'input' to print.
        print(f"Game started. Player is {player}")

        # (AH) Loop is for each keystroke at a time.
        while self._keep_playing:
            self._get_inputs()
            # (AH) update to compare only when typed <enter>.
            if self.input_service.get_letter() == "*":
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

        # Agnes check with Sarah's code.
        self.letter = self.input_service.get_letter()
        if self.letter.isalpha():
            self._buffer.update_buffer(self.letter)

    def _do_updates(self):
        """Updates the important game information for each round of play.
        In this case, that means checking that word typed by player
        in Buffer is the same as the random word from the word list.

        Args:
            self (Director): An instance of Director.
        """
        # (AH) player_input is what player typed and is stored in Buffer Class.
        player_input = self._buffer.get_buffer()
        # (AH) player_input is compared to the key of the Words dictionary.
        if player_input in self.words.get_words():
            # (AH) if player_input correct, increment score.
            self.scoreboard.add_score(1)
            # (AH) clear the Buffer list for next round of play.
            self.buffer.flush_buffer()

    def _do_outputs(self):
        """Outputs the important game information for each round of play.
        In this case, that means checking the five random words falling down
        on the screen have not yet been typed by the player.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_top()
        self._output_service.draw_word()
        self._output_service.draw_bottom()
        self._output_service.flush_buffer()
