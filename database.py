# Database Class description
# attributes
# word	: word
#
# methods
# read_file	: read text file
# word_list	: store words in to a list
# add_word	: add a update word to a file

# from word import Word
# from solver import Solver

class Database:
    # def __init__(self, word=''):
    #     self.word = word
    #
    # def read_file(self, file_name):
    #     with open(file_name, 'r') as f:
    #         for line in f:
    #             self.word = line.strip()
    #
    # def word_list(self):
    #     return self.word
    #
    # def add_word(self, file_name):
    #     with open(file_name, 'a') as f:
    #         f.write(self.word + '')

    def __init__(self, word=''):
        self.word = word

    def read_file(self, file_name):
        with open(file_name, 'r') as f:
            for line in f:
                self.word.append(line.strip())
        return self.word

    def add_word(self, file_name):
        with open(file_name, 'a') as f:
            f.write(self.word + '')

    def __repr__(self):
        return self.word
