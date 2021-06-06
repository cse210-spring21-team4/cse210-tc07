from game.console import Console
from game.roster import Roster
from game.leaderboard import Leaderboard
import inquirer


class Menu(Console):
    """The Menu class extends the Console class, to encompass all console prints
    and input validation/collection. It prints a menu to the terminal, allowing
    players to create/select/delete profiles, view leaderboard rankings, access
    a game rules page, start a round of play, or quit.

    ATTRIBUTES
    player : str
        The selected player profile, passed to Director class for gameplay.
    initial : bool
        Indicates whether class is running for the first time. Used to set logo
        animation to a unique "opening game" style
    quit_menu : bool
        Indicates whether to continue displaying main menu screen.
    play_game : bool
        Indicates whether game will start after exiting menu.
    margin : str
        Set number of blank spaces, used for terminal display formatting.
        """
    def __init__(self):
        super().__init__()
        self._roster = Roster()
        self._scores = Leaderboard()

        self.player = ""
        self.__initial = True
        self.__quit_menu = False
        self.__play_game = True
        self.__margin = " " * 5

    def main_menu(self) -> bool:
        """
        main_menu calls the show_menu method to display the parent menu.

        The method loops through menu display until the player exits the game
        or starts a round of gameplay.
        Returns:
            bool: indicates whether to start gameplay or exit the program.
        """
        while not self.__quit_menu:
            self.__show_menu()
            self.__initial = False
        self.__initial = True
        return self.__play_game

    def __show_menu(self) -> None:
        """
        __show_menu displays the parent menu.

        Depending on the players selection in the menu, this method will adjust
        the appropriate class attributes and call other methods to start play,
        end the program, or view a sub-menu.
        """
        self.clear_screen()
        self.print_logo(left=5, cool=self.__initial)
        self.__print_player()
        select = self.__get_selection()

        if select == "start":
            self.__quit_menu = True
        elif select == "select":
            self.player = self._roster.show_roster_menu()
        elif select == "rules":
            self.__show_rules()
        elif select == "scores":
            self._scores.show_leaderboard()
        elif select == "quit":
            self.clear_screen()
            self.__quit_menu = True
            self.__play_game = False
            input("Game quit")

    def __print_player(self) -> None:
        """__print_player prints title text for the main menu."""
        if not self.player:
            self.cool_print("NO PLAYER SELECTED. SELECT/ADD PLAYER.")
        else:
            name = self.player.upper()
            self.cool_print(f"WELCOME {name}. Select START to begin round.")
        self.pause(.2)
        print()

    def __get_selection(self):
        """
        __get_selection displays the interactive menu in __show_menu.

        It does so by implementing the imported Inquirer library, which can be
        found at https://pypi.org/project/inquirer/

        Returns:
            str: A string of text indicating the selected option.
        """
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
        """Loads the rules.txt file from assets/ and prints it to terminal."""
        self.clear_screen()
        self.print_logo()
        for line in self.load_asset("rules"):
            print(self.__margin + line, end="")
        input()
