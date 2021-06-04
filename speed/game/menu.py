from game.console import Console


class Menu(Console):
    """A code template for a person who directs the game. The responsibility of
        this class of objects is to control the sequence of play.

        Stereotype:
            Service Provider, Interfacer

        Attributes:
            roster (Roster): An instance of the Console class.
        """

    def __init__(self):
        """The class constructor.

        Args:
            self (Console): an instance of Console.
        """
        super().__init__()
        self.stop_game = False
        self.__show_menu = True
        self.__logo = []
        self.__fame = []
        self.__rules = []

        # with open("mastermind/assets/logo.txt") as data:
        #     next(data)
        #     for line in data:
        #         self.__logo.append(line)

        # with open("mastermind/assets/fame.txt") as data:
        #     next(data)
        #     for line in data:
        #         self.__fame.append(line)

        # with open("mastermind/assets/rules.txt") as data:
        #     next(data)
        #     for line in data:
        #         self.__rules.append(line)

    def main_menu(self):
        input("MENU WILL APPEAR HERE.")