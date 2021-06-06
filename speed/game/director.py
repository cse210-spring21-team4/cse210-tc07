from time import sleep

from game import constants
from game.words import Words
from game.scoreboard import Scoreboard


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

    def __init__(self, input_service, output_service, player: str):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self._scoreboard = Scoreboard(player)
        self._words = Words()
        self._input_service = input_service
        self._output_service = output_service

        self._keep_playing = True

        self.check_guess = False
        self.buffer = []
        self.buffer_text = ""

        self.words_per_min = 8
        self.word_rate = self.__get_word_rate()
        self.cycle_count = self.word_rate - 15
        self.fall_rate = 8
        self.fall_count = 0

        self.player = player

    def start_game(self):
        """Starts the game loop to control the sequence of play.

        ARGS
        player : str
            The username of a selected player profile.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates(self.player)
            self._do_outputs(self.player)
            self.cycle_count += 1
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """
        Gets the keyboard input at the beginning of each play cycle.
        If input is a letter, it is added to the buffer.
        """
        self.check_guess = False
        letter = self._input_service.get_letter()
        if letter.isalpha():
            self.buffer.append(letter)
        if letter == "*":
            self.check_guess = True

    def _do_updates(self, player: str):
        """
        _do_updates Updates score based on player guess

        Consolidates the input buffer into a string, and passes it to the Words
        class to see if the string is a valid guess. Upon confirmation, an int
        is returned and added to the score. Then the input buffer is cleared.
        """
        should_fall = False
        self.fall_count += 1
        if self.fall_count == (self.fall_rate - 1):
            should_fall = True
            self.fall_count = 0

        strikes = self._words.update_positions(should_fall)
        self._scoreboard.add_strikes(strikes)

        if self.cycle_count == self.word_rate:
            self._words.add_word(self._scoreboard.get_level())
            self.cycle_count = 0

        player_input = "".join(self.buffer)
        if self.check_guess:
            points = self._words.check_guess(player_input)
            if points:
                self._scoreboard.add_score(points)
            self.buffer = []

        self.buffer_text = player_input.ljust(constants.MAX_X, "-")

    def _do_outputs(self, player: str):
        """Outputs the important game information for each round of play.
        In this case, that means checking the five random words falling down
        on the screen have not yet been typed by the player.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()

        level = self._scoreboard.get_level()
        score = self._scoreboard.get_score()
        strikes = self._scoreboard.get_strikes()

        self._output_service.draw_top(self.player, level, score, strikes)
        self._output_service.draw_word(self._words.get_words())
        self._output_service.draw_bottom(self.buffer_text)
        self._output_service.flush_buffer()
        print(self.cycle_count)

    def __get_word_rate(self):
        return int(((60 / constants.FRAME_LENGTH) / self.words_per_min)) - 1
