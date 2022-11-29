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


class Solver:
    def __init__(self, word_lst):
        self.word_lst = []
        self.question = ""
        self.question_lst = []
        self.answer = ""
        self.answer_lst = []

    def split(self, word):
        for i in word:
            self.question_lst.append(i)

    def ask_and_lower(self):
        self.answer = input("Enter a word: ").lower()
        for i in self.answer:
            self.answer_lst.append(i)

    def check_real(self):
        if self.answer in self.word_lst:
            return True
        else:
            return False

    def check_five(self):
        if len(self.answer) == 5:
            return True
        else:
            return False

    def split_input(self):
        for i in self.answer:
            self.answer_lst.append(i)

    def eliminate_g(self, lst, ans):
        num = ['1', '2', '3', '4', '5', '-']
        green = input('Input green tile index(es) (if not input -) : ')
        index = [i for i in green]

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
            letter_correct = []
            for i in index:
                letter_correct.append(ans[i - 1])

            for i in range(len(lst)):
                for j in range(len(letter_correct)):
                    if letter_correct[j] not in lst[i]:
                        lst[i] = 'x'
                    elif lst[i][index[j] - 1:index[j]] != letter_correct[j]:
                        lst[i] = 'x'

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
            letter_correct = []
            for i in index:
                letter_correct.append(ans[i - 1])

            for i in range(len(lst)):
                for j in range(len(letter_correct)):
                    if lst[i] == 'x':
                        pass
                    elif letter_correct[j] not in lst[i]:
                        lst[i] = 'x'
                    elif lst[i][index[j] - 1:index[j]] == letter_correct[j]:
                        lst[i] = 'x'


# x = Solver(Database().word_list)
#
# x.ask_and_lower()
# x.check_five()
# x.check_real()
# x.split_input()
# x.eliminate_g(x.word_lst, x.answer_lst)
