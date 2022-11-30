# Word Class description
# attributes
# word	: list containing all 5-letter words
#
# methods
# getter&setter

# from database import Database


class Word:
    def __init__(self, word):
        self.__word = word

    @property
    def word(self):
        return self.__word

    @word.setter
    def word(self, word):
        self.__word = word

    # def check(self):
    #     if self.word in Database.read_file('sgb-words.txt') and len(self.word) == 5:
    #         return True
    #     else:
    #         return False

    def __repr__(self):
        return self.word
# word_class_list = []
# solver = Solver()
# for i in slover.word_lst:
#     word_class_list.append(Word(i))

# print(Database.read_file('sgb-words.txt'))
