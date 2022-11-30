from word import Word


class Database:  # Database Class description
    def __init__(self, filename=''):  # constructor
        self.filename = filename
        self.word_lst = []

    def read_file(self, file_name):  # read file
        with open(file_name, 'r') as f:
            lst = []
            for line in f:
                lst.append(Word(line.strip()))
        self.word_lst = lst
        return self.word_lst

    def add_word(self, word, file_name):  # add word to file
        with open(file_name, 'a') as f:
            f.write(word)

    def __repr__(self):  # return string representation of object
        return self.word_lst
