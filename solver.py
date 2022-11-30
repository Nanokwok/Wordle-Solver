# Solver Class description
# attributes
# word_list	: list containing object from Word class
# question(str)	: question in the game
# answer(str)	: answer of user
#
# methods
# split 	: split question into a list that have 5 indexes
# ask_and lower	: ask user input and  lower the input
# check_real 	: Check if the input that the user enters is a real 		word (is it in the word_list)
# check_five	: Check if the input that the user enters has 5 		characters
# split_input	: split input into a list that have 5 indexes
# eliminate_g	: eliminate word that not in the right spot
# 	ex. f ‘L’ o a t → eliminate word that don’t have ‘L’ in 	second letter
# eliminate_y	: eliminate word that letter in the yellow spot and the 	word that don’t have that letter in the word (yellow 	spot is letter that not in the right place but in the 	word)
# 	ex. f L o a t → eliminate word that have ‘L’ in		second letter and eliminate word that don’t have ‘L’ 	in word

# from database import Database
from word import Word

# solver_lst = []

class Solver:
    def __init__(self, word):
        self._word_lst = []
        self.question = ''
        self.answer = ''
        self.question_lst = []
        self.answer_lst = []
        self.word = word

    @property
    def word_list(self):
        return self._word_lst

    @word_list.setter
    def word_list(self, lst):
        self._word_lst = lst

    # def split(self, word):
    #     for i in word:
    #         self.question_lst.append(i)

    def ask_and_lower(self):
        self.answer = input("Enter a word: ").lower()
        for i in self.answer:
            self.answer_lst.append(i)

    def check_real(self, word, lst):
        if word in lst:
            return True
        else:
            return False

    def check_five(self, word):
        if len(word) == 5:
            return True
        else:
            return False

    def split_input(self):
        for i in self.answer:
            self.answer_lst.append(i)

    # def word(self):
    #     for i in self.word_lst:
    #         self.word_lst.append(Word(i))
    def update(self):
        for word in self.word:
            self._word_lst.append(word)

    def add_word(self, word):
        self._word_lst.append(word)


    def eliminate_g(self, lst, ans):
        num = ['1', '2', '3', '4', '5', '-']
        green = input('Input green tile index(es) (if not input -) : ')
        index = [i for i in green]
        # if len(dump) != 0:
        #     for i in dump:
        #         index.append(i)

        bool = all(i in num for i in index)

        while not bool:
            print('Invalid input')
            green = input('Input green tile index(es) (if not input -) : ')
            index = [i for i in green]
            bool = all(i in num for i in index)

        if green != '-':
            for i in range(len(index)):
                index[i] = int(index[i])

        if green == '-':
            pass
        else:
            # if len(dump) != 0:
            #     for i in dump:
            #         index.append(i)

            letter_correct_g = []
            for i in index:
                letter_correct_g.append(ans[i - 1])

            for i in range(len(lst)):
                for j in range(len(letter_correct_g)):
                    if letter_correct_g[j] not in lst[i]:
                        # counts = 0
                        # for k in range(len(lst[i])):
                        #     if lst[i][k] == letter_correct_g[j]:
                        #         counts += 1
                        # if counts == 1:
                        lst[i] = 'x'
                    elif lst[i][int(index[j]) - 1:int(index[j])] != letter_correct_g[j]:
                        lst[i] = 'x'
        return index

    def eliminate_y(self, lst, ans):
        num = ['1', '2', '3', '4', '5', '-']
        yellow = input('Input yellow tile index(es) (if not input -) : ')
        index = [i for i in yellow]

        bool = all(i in num for i in index)

        while not bool:
            print('Invalid input')
            yellow = input('Input yellow tile index(es) (if not input -) : ')
            index = [i for i in yellow]
            bool = all(i in num for i in index)

        if yellow != '-':
            for i in range(len(index)):
                index[i] = int(index[i])

        if yellow == '-':
            pass
        else:
            # if len(dump) != 0:
            #     for i in dump:
            #         index.append(i)

            letter_correct_y = []
            for i in index:
                letter_correct_y.append(ans[i - 1])

            for i in range(len(lst)):
                for j in range(len(letter_correct_y)):
                    if lst[i] == 'x':
                        pass
                    elif letter_correct_y[j] not in lst[i]:
                        # counts = 0
                        # for k in range(len(lst[i])):
                        #     if lst[i][k] == letter_correct_y[j]:
                        #         counts += 1
                        # if counts == 1:
                        lst[i] = 'x'
                    elif lst[i][index[j] - 1:index[j]] == letter_correct_y[j]:
                        lst[i] = 'x'
        return index

    def eliminate_b(self, lst, ans, g_index, y_index):
        need = []
        for i in g_index:
            need.append(i)
        for i in y_index:
            need.append(i)

        not_need = []
        for i in range(1, 6):
            if i not in need:
                not_need.append(i)

        char = []
        for i in not_need:
            char.append(ans[i - 1: i])

        for i in range(len(lst)):
            for j in char:
                if j in lst[i]:
                    lst[i] = 'x'

    def display_word(self, ans, g_index, y_index):
        for i in range(1, 6):
            if i in g_index:
                print(f"'{(ans[i - 1:i]).upper()}'", end=' ')
            elif i in y_index:
                print((ans[i - 1:i]).upper(), end=' ')
            else:
                print(ans[i - 1:i], end=' ')
        print()

    def update_word_lst(self, lst):
        word = []
        for i in lst:
            if i != 'x':
                word.append(i)
        lst = word
        return lst

# x = Solver(Database().word_list)
#
# x.ask_and_lower()
# x.check_five()
# x.check_real()
# x.split_input()
# x.eliminate_g(x.word_lst, x.answer_lst)
