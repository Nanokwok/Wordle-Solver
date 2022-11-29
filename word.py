# Word Class description
# attributes
# word	: list containing all 5 letter words
#
# methods
# getter&setter

from database import Database
# from solver import Solver


class Word:
    def __init__(self):
        self.word = Database.read_file('sgb-words.txt')

    @property
    def word(self):
        return self.word

    @word.setter
    def word(self, word):
        self.word = word

    def __repr__(self):
        return self.word


print(Database.read_file('sgb-words.txt'))
