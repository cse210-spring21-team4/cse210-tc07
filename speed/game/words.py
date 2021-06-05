from random import sample, randint


class Words:
    """
    Words is a class for words.
    """
    def __init__(self):
        self.__pool = self.__load_words()
        self.__words = {}

    def get_words(self):
        return self.__words

    def add_word(self, level=int):
        unlocked = []
        for key in self.__pool:
            if key <= level:
                unlocked.extend(self.__pool[key])
        new_word = sample(unlocked, 1)
        x = self.__get_x(new_word)
        self.__words[new_word] = (x, 21)

    def update_positions(self):
        for item in self.__words.keys():
            x, y = self.__words[item]
            if y == 0:
                self.__words.pop(item)
            else:
                self.__words[item] = (x, y - 1)

    def check_guess(self, word=str):
        if word in self.__words:
            self.__words.pop(word)
            return len(word)

    def __get_x(self, word=str):
        return randint(0, (61 - len(word)))

    def __load_words(self):
        with open("speed/assets/words.txt") as text:
            word_list = text.read().splitlines()
            word_list.sort(key=len)
        pool = {}
        for word in word_list:
            if len(word) not in pool:
                pool[len(word)] = []
            if word not in pool[len(word)]:
                pool[len(word)].append(word)
        return pool
