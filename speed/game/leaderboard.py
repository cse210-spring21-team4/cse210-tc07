from datetime import datetime
from json import load, dump
import inquirer

from game.console import Console


class Leaderboard(Console):
    def __init__(self):
        super().__init__()
        self.__board = self.__load_leaderboard()

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

    def __load_leaderboard(self):
        with open("speed/assets/leaderboard.json", "r") as data:
            entries = load(data)
        if entries is not None:
            return entries
        else:
            return {}
