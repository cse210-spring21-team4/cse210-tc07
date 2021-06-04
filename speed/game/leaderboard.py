from datetime import datetime
from json import load, dump
import inquirer

from game.console import Console


class Leaderboard(Console):
    def __init__(self):
        super().__init__()
        self.__board = self.__load_leaderboard()

    def new_entry(self, player=str, score=int:
        pass

    def __load_leaderboard(self):
        with open("speed/assets/leaderboard.json", "r") as data:
            entries = load(data)
        if entries is not None:
            return entries
        else:
            return {}