from random import choice, randint
from game import constants


class Words:
    """
     The Words class tracks and updates words on screen, and their positions.

    The class loads in a text file of words, divides them by length, and then
    adds words to a dictionary, along with X/Y coordinates. This dictionary is
    what Director passes to Output_Service, to print words to screen.

    Word class also updates word positions (i.e. makes them fall down), checks
    player guesses, determines points for correct guesses, and removes words
    that have fallen off of the screen or that have been correctly typed.

    ATTRIBUTES
    pool : dict
        Dictionary of words, grouped in lists by length. Structured as follows:
            {word_length: [list of words]} --[for example]-->
            {1: ["a", "b"], 2: ["at", "if"], 3: ["cat", "rag"]}
    words : dict
        Dictionary of active words (str) and their coordinates (tuple):
        {word: (x_coord, y_coord)} --[for example]-->
        {"apple": (47, 15), "nail": (2, 6), "koala": (19, 12)}
    """
    def __init__(self):
        self.__pool = self.__load_words()
        self.__words = {}

    def get_words(self):
        return self.__words

    def add_word(self, level: int) -> None:
        """
        add_word  takes a level of difficulty as an integer, then finds a word
        corresponding difficulty in __pool and adds it to __words.

        When adding the word, the __get_x method is called to determine an
        appropriate x coordinate. The y coordinate is set to 21, which is off
        of the screen. These coordinates are added to the __words dictionary as
        a (tuple) value, with the word itself as the (string) key.

        Args:
            level (int): The level (or rank) of difficult. Indicated how much
            of the __pool of words should be unlocked to randomly select from.
        """
        unlocked = []
        for key in self.__pool:
            if key <= level:
                unlocked.extend(self.__pool[key])
        new_word = choice(unlocked)
        x = self.__get_x(new_word)
        self.__words[new_word] = (x, 0)

    def update_positions(self) -> int:
        """
        update_positions subtracts 1 from the y coordinate of each word in the
        words dictionary. Any words that have fallen to the bottom of the
        screen (where Y equals zero) are removed from the dictionary.

        At the end of execution, this method returns the total number of words
        that have fallen off as an int, which are used to determine the strikes
        a player receives.
        """
        strikes = 0
        for item in list(self.__words.keys()):
            x, y = self.__words[item]
            if y == constants.MAX_Y + 1:
                self.__words.pop(item)
                strikes += 1
            else:
                self.__words[item] = (x, y + 1)
        return strikes

    def check_guess(self, word: str) -> int:
        """
        check_guess determines if a given word exists in the __words dictionary

        If the word is found in the dictionary, the entry is removed and an
        the word length (as an integer of the "points" the word is worth) is
        returned. If the guess is incorrect, the method returns None.

        Args:
            word (string): The typed word to be checked.

        Returns:
            int: Points for a correct guess
        """
        if word in self.__words:
            self.__words.pop(word)
            return len(word)

    def __get_x(self, word: str) -> int:
        """Returns random X coord. for entire given word to appear onscreen."""
        return randint(0, (constants.MAX_X + 1 - len(word)))

    def __load_words(self) -> dict:
        """
        __load_words uses a list of words from the assets/ directory to create
        a dictionary of word list, grouped in by word length.

        Returns:
            dict: Dictionary of words, grouped in lists by length.

                Dictionary structure is as follows:
                {word_length: [list of words]} --[for example]-->
                {1: ["a", "b"], 2: ["at", "if"], 3: ["cat", "rag"]}
        """
        with open("speed/assets/words.txt") as text:
            word_list = text.read().splitlines()
            word_list.sort(key=len)
        pool = {}
        for word in word_list:
            if len(word) not in pool:
                pool[len(word)] = []
            if word not in pool[len(word)]:
                pool[len(word)].append(word)
        return pool
