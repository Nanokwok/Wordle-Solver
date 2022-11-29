# Word Class description
# attributes
# word	: list containing all 5-letter words
#
# methods
# getter&setter

from database import Database
# from solver import Solver


class Word:
    def __init__(self, word):
        self.word = word

    # @property
    # def word(self):
    #     return self.word
    #
    # @word.setter
    # def word(self, word):
    #     self.word = word
    def check(self):
        if self.word in Database.read_file('sgb-words.txt') and len(self.word) == 5:
            return True
        else:
            return False

    # def __repr__(self):
    #     return self.word


# print(Database.read_file('sgb-words.txt'))
