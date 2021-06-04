class Roster:
    """A code template for a person who directs the game. The responsibility of
    this class of objects is to control the sequence of play.

    Stereotype:
        Service Provider, Interfacer

    Attributes:
        roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Console): an instance of Console.
        """
        self.__players = []

    def get_roster(self):
        """ Returns the list of players.

        Args:
            self (Roster): an instance of Roster.
        """
        return self.__players
