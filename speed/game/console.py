import os
from time import sleep
from sys import stdout


class Console:
    """
     The Console class contains basic methods terminal printing, as well as for
    loading text file assets and parsing those assets for display.

    Attributes:
    logo : list
        an ASCII art logo, stored line-by-line in a list.
    """

    def __init__(self):
        """The class constructor."""
        self.__logo = self.load_asset("logo")

    def load_asset(self, asset: str) -> list:
        """Private method for loading a given asset from assets folder.
        Returns a list, loaded with lines from selected text file.

        Args:
        asset : String
            name of the .txt file to be loaded.
        """
        path = f"speed/assets/{asset}.txt"
        new_list = []

        with open(path) as data:
            next(data)
            for line in data:
                new_list.append(line)

        return new_list

    def pause(self, seconds: float) -> None:
        """Pauses operations for given number of seconds. """
        sleep(seconds)

    def clear_screen(self) -> None:
        """Detects OS type and sends console command to clear screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def cool_print(self, text: str, newline: bool = True, margin: int = 5,
                   rate: float = .02):
        """Prints text to the console in typewriter style.

        Args:
        text : str
            Text to print.
        newline : bool
            Optional; Whether to add carriage return at end of line
        margin : int
            Optional; Number of spaces of offset line from left of screen.
        rate : float
            Optional; Speed (seconds )at which printing occurs.
        """
        print(" " * margin, end='')
        for letter in text:
            sleep(.02)
            stdout.write(letter)
            stdout.flush()
        if newline:
            print()

    def print_logo(self, left: int = 5, top: int = 1, bottom: int = 1,
                   cool: bool = False, factor: float = .8, logo: list = []
                   ) -> None:
        """Prints logo to screen. Has "cool" mode for a more interesting print.
        Print the SPEED logo by default, but different logo can be specified.

        Args:
        left : int
            Optional; Number of spaces to offset logo from left of screen
        top : int
            Optional; Number of lines to offset logo from top of screen
        bottom : int
            Optional; Number of lines to print after logo
        cool : bool
            Optional; If True, printing occurs in a line-by-line "reveal".
        factor : float
            Optional; Acceleration rate of "cool" printing. (For example, the
            default .8 rate means that each line prints in 80% of the time of
            the previous line.)
        logo : list of strings
            Optional; Used to specify an alternate logo or header, which must
            be a list of strings.
        """
        text = logo if logo else self.__logo

        print('\n' * top, end="")
        margin = " " * left
        if cool:
            time = .3
            for line in text:
                stdout.write(margin)
                stdout.write(line)
                stdout.flush()
                sleep(time)
                time *= factor
            sleep(.3)
        else:
            for line in self.__logo:
                print(margin + line, end="")

        print('\n' * bottom, end="")
