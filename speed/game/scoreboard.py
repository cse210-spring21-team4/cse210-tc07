class Scoreboard:
    """
     The Scoreboard class tracks score and strikes during gameplay

    It should not be confused with the Leaderboard class, which is responsible
    for storing scores *between* rounds of gameplay.

    ARGS
    player : str
        The name (i.e. username) of the player for the round.

    ATTRIBUTES
    player : str
        Passed into class as argument during instantiation.
    score : int
        A positive integer, indicates current score during gameplay.
    level : int
        A positive integer, indicates current rank/level during gameplay.
    strikes : int
        A positive integer, indicates the number of strikes during gameplay.
    ranks : dict
        Dictionary of ranks/levels, corresponding to the minimum score needed
        to reach that level.
    """
    def __init__(self, player: str):
        self.__player = player
        self.__score = 0
        self.__level = 1
        self.__strikes = 0
        self.__ranks = {(n-1)*25: n for n in range(1, 21)}

    def get_score(self) -> int:
        return self.__score

    def get_level(self) -> int:
        return self.__level

    def get_strikes(self) -> int:
        return self.__strikes

    def add_strike(self) -> None:
        self.__strikes += 1

    def add_score(self, points: int) -> None:
        """
        add_score increments score by given number of points, then checks to
        see if the new score will move the player into a new rank. If a new
        rank has been achevied, the self.__level attribute is updated.

        Args:
            points (int): number to add to score
        """
        self.__score += len(points)

        for rank in self.__ranks.keys():
            if self.__score >= rank:
                self.__level = self.__ranks[rank]
            else:
                break
