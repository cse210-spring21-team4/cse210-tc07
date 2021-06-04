import os
from time import sleep
from sys import stdout


class Console:
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
        self.__logo = self.load_asset("logo")

    def load_asset(self, asset=str):
        """Private method for loading a given asset from assets folder.
        Returns a list, loaded with lines from selected text file.

        Args:
            self (Console): an instance of Console.
            asset (string): name of the .txt file to be loaded.
        """
        path = f"speed/assets/{asset}.txt"
        new_list = []

        with open(path) as data:
            next(data)
            for line in data:
                new_list.append(line)

        return new_list

    def pause(self, seconds=float):
        """Detects OS type and sends appropriate console command to clear screen.

        Args:
            self (Console): An instance of Console.
        """
        sleep(seconds)

    def clear_screen(self):
        """Detects OS type and sends appropriate console command to clear screen.

        Args:
            self (Console): An instance of Console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def cool_print(self, text=str, newline=True, margin=5, rate=.02):
        """Prints text in typewriter style.

        Args:
            self (Console): an instance of Console.
            text (str): Text to print.
            newline (bool): whether to end with carriage return
        """
        print(" " * margin, end='')
        for letter in text:
            sleep(.02)
            stdout.write(letter)
            stdout.flush()
        if newline:
            print()

    def print_logo(self, left=5, top=1, bottom=1,
                   cool=False, factor=.8, logo=[]):
        """Prints logo to screen. Has optional x and y parameters to offset logo
        by specified amount of lines and spaces.

        Args:
            self (Console): An instance of Console.
            left (int): Number of spaces to offset logo from left of screen
            top (int): Number of lines to offset logo from top of screen
            bottom (int): Number of spaces to print below logo
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
