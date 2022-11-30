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

    def ask_and_lower(self):  # ask for question and convert to lower case
        self.answer = input("Enter a word: ").lower()  # input answer
        for i in self.answer:  # split answer
            self.answer_lst.append(i)

    def split_input(self):  # split input
        for i in self.answer:
            self.answer_lst.append(i)

    def update(self):  # update word list
        for word in self.word:
            self._word_lst.append(word)

    def add_word(self, word):  # add word to word list
        self._word_lst.append(word)

    def eliminate_g(self, lst, ans):  # eliminate green
        num = ['1', '2', '3', '4', '5', '-']
        green = input('Input green tile index(es) (if not input -) : ')
        index = [i for i in green]

        bool = all(i in num for i in index)  # check if input is valid

        while not bool:
            print('Invalid input')
            green = input('Input green tile index(es) (if not input -) : ')
            index = [i for i in green]  # split input
            bool = all(i in num for i in index)  # check if input is valid

        if green != '-':  # if input is not '-'
            for i in range(len(index)):  # convert to int
                index[i] = int(index[i])

        if green == '-':
            pass
        else:  # if input is not '-'
            letter_correct_g = []  # list of correct letter
            for i in index:
                letter_correct_g.append(ans[i - 1])  # append correct letter to list

            for i in range(len(lst)):  # eliminate word
                for j in range(len(letter_correct_g)):  # check if letter is correct
                    if letter_correct_g[j] not in lst[i]:  # if letter is not in word
                        lst[i] = 'x'  # eliminate word
                    elif lst[i][int(index[j]) - 1:int(index[j])] != letter_correct_g[j]:
                        # if letter is not in correct position
                        lst[i] = 'x'  # eliminate word
        return index

    def eliminate_y(self, lst, ans):  # eliminate yellow
        num = ['1', '2', '3', '4', '5', '-']
        yellow = input('Input yellow tile index(es) (if not input -) : ')
        index = [i for i in yellow]

        bool = all(i in num for i in index)

        while not bool:  # check if input is valid
            print('Invalid input')
            yellow = input('Input yellow tile index(es) (if not input -) : ')
            index = [i for i in yellow]
            bool = all(i in num for i in index)

        if yellow != '-':  # if input is not '-'
            for i in range(len(index)):
                index[i] = int(index[i])

        if yellow == '-':  # if input is '-'
            pass
        else:  # if input is not '-'
            letter_correct_y = []
            for i in index:
                letter_correct_y.append(ans[i - 1])  # append correct letter to list

            for i in range(len(lst)):
                for j in range(len(letter_correct_y)):
                    if lst[i] == 'x':
                        pass
                    elif letter_correct_y[j] not in lst[i]:  # if letter is not in word
                        lst[i] = 'x'
                    elif lst[i][index[j] - 1:index[j]] == letter_correct_y[j]:  # if letter is in correct position
                        lst[i] = 'x'
        return index

    def eliminate_b(self, lst, ans, g_index, y_index):
        need = []  # list of letter that need to be eliminated
        for i in g_index:  # append letter in green index to list
            need.append(i)
        for i in y_index:  # append letter in yellow index to list
            need.append(i)

        not_need = []  # list of letter that do not need to be eliminated
        for i in range(1, 6):
            if i not in need:  # if letter is not in green or yellow index
                not_need.append(i)  # append letter to list

        char = []  # list of letter that need to be eliminated
        for i in not_need:
            char.append(ans[i - 1: i])

        for i in range(len(lst)):
            for j in char:
                if j in lst[i]:
                    lst[i] = 'x'

    def display_word(self, ans, g_index, y_index):  # display word
        for i in range(1, 6):
            if i in g_index:  # if letter is in green index
                print(f"'{(ans[i - 1:i]).upper()}'", end=' ')  # print letter in upper case with quote
            elif i in y_index:  # if letter is in yellow index
                print((ans[i - 1:i]).upper(), end=' ')  # print letter in upper case
            else:  # if letter is not in green or yellow index
                print(ans[i - 1:i], end=' ')  # print letter in lower case
        print()  # print new line

    def update_word_lst(self, lst):  # update word list
        word = []
        for i in lst:
            if i != 'x':
                word.append(i)
        lst = word
        return lst
