from datetime import datetime
from json import load, dump

from game.console import Console


class Leaderboard(Console):
    """The Leaderboard is stores and ranks the high score data. In addition to
    providing a way of storing and retrieving score data in the assets/ folder,
    it also provides methods for displaying score rankings to the console,
    which is why Leaderboard is an extension of the Console superclass.

    Args:
        Console (Class): An instance of the Console class, which handles CLI
            printing.
    """
    def __init__(self):
        """The class constructor

        Vars:
            self.__board: A dictionary of score/player rankings
            self.__header: A dictionary of score/player rankings
        """
        super().__init__()
        self.__board = self.__load_leaderboard()
        self.__header = self.load_asset("hi_scores")

    def new_entry(self, player=str, score=int):
        timestamp = datetime.now().strftime("%b %-d %Y  %Y%m%d%H%M%S")

        self.__leaderboard.update(
            {timestamp: {
                "score": score,
                "player": player}})

        new_dict = {k: v for (k, v) in sorted(
                self.__leaderboard.items(),
                key=lambda x: x[1]["score"])}
        with open("mastermind/assets/leaderboard.json", "w") as data:
            dump(new_dict, data, indent=4)

        self.__board = self.__load_leaderboard()

    def show_leaderboard(self):
        self.clear_screen()
        self.print_logo(cool=True, factor=.7, logo=self.__header)
        self.__print_rankings()
        input()

    def __print_rankings(self, left=2):
        print()
        rankings = list(self.__board.items())[:10]
        lines_printed = 0
        for idx, (time_data, data) in enumerate(rankings):
            lines_printed += 1
            idx += 1
            margin = left * " "
            name = data["player"]
            score = data["score"]
            month, day, year, dt = time_data.split(" ")
            date = f"{month} {day} {year}"

            print(f"{margin}{idx:>3}. {name:<15} {score:^30} {date:>15}\n")
            self.pause(.1)
        lines = "\n" * (12 - lines_printed)
        print(lines, end="")
        self.pause(.5)
        self.cool_print("Press ENTER to return to player menu.",
                        newline=False, margin=5)

    def __load_leaderboard(self):
        with open("speed/assets/leaderboard.json", "r") as data:
            entries = load(data)
        if entries is not None:
            return entries
        else:
            return {}
