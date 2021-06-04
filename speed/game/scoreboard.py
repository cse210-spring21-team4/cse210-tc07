class Scoreboard:
    def __init__(self, player=str):
        self.__player = player
        self.__score = 0
        self.__level = 1
        self.__strikes = 0
        self.__ranks = {(n-1)*25: n for n in range(1, 21)}
        input(self.__ranks)

    def get_score(self):
        return self.__score

    def get_level(self):
        return self.__level

    def add_score(self, points=int):
        self.__score += len(points)
        if self.__score in self.__ranks:
            self.__level = self.__ranks[self.__score]

    def add_strike(self):
        self.__strikes += 1

    def get_strikes(self):
        return self.__strikes
