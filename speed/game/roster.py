from datetime import datetime
from json import load, dump
import inquirer

from game.console import Console


class Roster(Console):
    """
    Roster is the class responsible for players' user profiles. This class is
    built on the Console class, and has two primary functions:
        1. Load/Save player profile data to the assets/roster.json file
        2. Provide a menu for creating, deleting, and selecting player profiles

    ARGS
    Console : Class
        Class which handles CLI printing.

    ATTRIBUTES
    selected_player : str
        Name of selected player profile
    roster : dict
        Dictionary of user profiles, loaded from assets/roster.json
    show_menu : bool
        Indicates whether to continue displaying Roster menu in terminal
    """
    def __init__(self):
        super().__init__()
        self.__selected_player = ""
        self.__roster = self.__load_roster()
        self.__show_menu = True

    def get_players(self):
        if self.__roster:
            return list(self.__roster.keys())
        else:
            return []

    def show_roster_menu(self):
        while self.__show_menu:
            self.clear_screen()
            self.print_logo()

            selection = self.__roster_menu()

            if selection == "**back**":
                self.__show_menu = False
            elif selection == "**new**":
                self.__add_player()
            elif selection == "**delete**":
                self.__delete_menu()
            else:
                self.__selected_player = selection
                self.__show_menu = False

        self.__show_menu = True
        return self.__selected_player

    def __roster_menu(self):
        title = "Select a profile. Press ENTER to confirm"
        if self.__selected_player:
            name = self.__selected_player.upper()
            title = f"{name} selected."

        players_list = [("NEW PLAYER", "**new**")]
        players_list.extend(self.get_players())
        if self.get_players():
            players_list.extend([("DELETE PLAYER", "**delete**")])
        players_list.extend([("BACK", "**back**")])

        dft = self.__selected_player if self.__selected_player else "BACK"

        players = [
            inquirer.List(
                'selection',
                message=title,
                choices=players_list,
                default=dft,
                carousel=True)
            ]

        return inquirer.prompt(players)['selection']

    def __delete_menu(self):
        self.clear_screen()
        self.print_logo()
        title = "Select profile to remove. Press ENTER to confirm"

        players_list = self.get_players()
        players_list.extend([("BACK", "**back**")])

        players = [
            inquirer.List(
                'selection',
                message=title,
                choices=players_list,
                default="BACK",
                carousel=True)
            ]

        selection = inquirer.prompt(players)['selection']
        if selection != "**back**":
            self.__confirm_delete(selection)

    def __prompt_name(self):

        self.clear_screen()
        self.print_logo()

        name = input("[!] Enter new player name and press ENTER:\n\n     ")
        if not (2 < len(name) < 16):
            self.clear_screen()
            self.print_logo()
            print("Username must be between 3 and 15 characters.")
            input("Press ENTER to return to player menu.")
        elif name in self.get_players():
            self.clear_screen()
            self.print_logo()
            print("Player already exists.")
            input("Press ENTER to return to player menu.")
        else:
            return name

    def __add_player(self):
        self.clear_screen()
        self.print_logo()
        name = self.__prompt_name()
        if name is not None:
            self.__update_roster(name)

    def __confirm_delete(self, name=str):
        self.clear_screen()
        self.print_logo()
        delete = inquirer.confirm(
                f"Do you want to remove '{name}'?", default=True
                )
        if delete:
            self.__remove_player(name)
            input(f"'{name}' removed. Press ENTER to continue.")

    def __load_roster(self):
        with open("speed/assets/roster.json", "r") as data:
            entries = load(data)
        if entries is not None:
            return entries
        else:
            return {}

    def __update_roster(self, name=str):
        timestamp = datetime.now().strftime("%Y %m %d %H%M%S")
        entry = {name: timestamp}

        if self.get_players():
            new_roster = self.__roster
            new_roster.update(entry)
        else:
            new_roster = entry

        with open("speed/assets/roster.json", "w") as data:
            dump(new_roster, data, indent=4)
        self.__roster = self.__load_roster()

    def __remove_player(self, name=str):
        new_roster = self.__roster
        new_roster.pop(name)
        with open("speed/assets/roster.json", "w") as data:
            dump(new_roster, data, indent=4)
        self.__roster = self.__load_roster()
