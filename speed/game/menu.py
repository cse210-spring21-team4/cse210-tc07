from game.console import Console
from game.roster import Roster
import inquirer


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

        self._roster = Roster()

        self.player = ""
        self.__show = True
        self.__quit = False
        self.__margin = " " * 5

    def main_menu(self):
        while self.__show:
            self.show_menu()
        return self.__quit

    def show_menu(self):
        self.clear_screen()
        self.print_logo()
        self.print_player()
        select = self.get_selection()

        input(select)

    def print_player(self):
        print(self.__margin, end="")
        if not self.player:
            self.cool_print(
                f"{'Welcome to SPEED. Please select a player.':^60}",
                margin=0
                )
        else:
            self.cool_print(
                f"{'Welcome {self.player}. Select START to begin round.':^60}",
                margin=0
                )

    def get_selection(self):
        p_num = 0
        if self._roster.get_roster():
            p_num = len(self._roster.get_roster())
        add_text = "Add/Remove Players [" + str(p_num) + " registered]"

        choice_list = [
                (add_text, "add"),
                "Rules",
                ("Leaderboard", "scores"),
                "Quit"
                ]

        if self.player:
            choice_list.insert(0, "START")

        questions = [
            inquirer.List(
                'selection',
                message="MENU (Use ↑ and ↓ to select, ENTER to confirm)",
                choices=choice_list,
                carousel=True,
                default="add")
                ]

        return inquirer.prompt(questions)['selection'].lower()
