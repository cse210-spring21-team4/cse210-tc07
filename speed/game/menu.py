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
        self.__initial = True
        self.__quit_menu = False
        self.__play_game = True
        self.__margin = " " * 5

    def main_menu(self):
        while not self.__quit_menu:
            self.__show_menu()
            self.__initial = False
        self.__initial = True
        return self.__play_game

    def __show_menu(self):
        self.clear_screen()
        self.print_logo(cool=self.__initial)
        self.__print_player()
        select = self.__get_selection()

        if select == "start":
            self.__quit_menu = True
        elif select == "select":
            self.player = self._roster.show_roster_menu()
        elif select == "rules":
            self.__show_rules()
        elif select == "scores":
            pass
        elif select == "quit":
            self.clear_screen()
            self.__quit_menu = True
            self.__play_game = False
            input("Game quit")

    def __print_player(self):
        if not self.player:
            self.cool_print("NO PLAYER SELECTED.")
        else:
            name = self.player.upper()
            self.cool_print(f"WELCOME {name}. Select START to begin round.")
        self.pause(.2)
        print()

    def __get_selection(self):
        p_num = 0
        if self._roster.get_players():
            p_num = len(self._roster.get_players())
        add_text = "Select Player [" + str(p_num) + " registered]"

        choice_list = [
                (add_text, "select"),
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

    def __show_rules(self):
        self.clear_screen()
        self.print_logo()
        for line in self.load_asset("rules"):
            print(self.__margin + line, end="")
        input()
