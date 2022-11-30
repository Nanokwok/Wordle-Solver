class Word:
    def __init__(self, word):
        self.__word = word

    @property  # getter
    def word(self):
        return self.__word

    @word.setter  # setter
    def word(self, word):
        self.__word = word

    def __repr__(self):
        return self.word
