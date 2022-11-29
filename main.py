from database import Database
# from word import Word
from solver import Solver
import random


def run(filename):
    print('Hello ! welcome to WORDLE SOLVER')
    print('================================')
    print('menu:')
    print('open slover [1]')
    print('display all word in a file [2]')
    print('add new word to a file [3]')
    menu_choice = input('What you selected : ')
    print('================================')
    if menu_choice == '1':
        rounds = 1
        # word_lst = Database.read_file(filename)
        with open(filename, 'r') as f:
            word_lst = []
            for line in f:
                word_lst.append(line.strip())
        while True:
            # if rounds == 1:
            ans = []
            print('good starting words to use for Wordle…')
            print('dealt [1]')
            print('roate [2]')
            print('store [3]')
            print('ocean [4]')
            print('((Your own guess)) [5]')
            yes_or_no = input('Have you won? (y/n) : ')
            if yes_or_no == 'y':
                print('Congratulations!')
                break
            elif yes_or_no == 'n':
                print('What you selected : ')
                print('Suggested words…')











    elif menu_choice == '2':
        # display all word in a file
        print('display all word in a file [1]')
        print('display just letter word in a file [2]')
        inp = input('What you selected : ')
        print('================================')
        if inp == '1':
            with open(filename, 'r') as f:
                lst = []
                for line in f:
                    lst.append(line.strip())
            # lst = Database.read_file('sgb-words.txt')

            for i in range(1, len(lst)):
                if i % 15 == 0:
                    print(lst[i])
                else:
                    print(lst[i], end=', ')
            print()
            print(f'There are "{len(lst)}" words in the file')

        elif inp == '2':
            letter = input('Enter a letter : ')
            with open(filename, 'r') as f:
                lst = []
                for line in f:
                    if line[0] == letter:
                        lst.append(line.strip())
            # lst = Database.read_file('sgb-words.txt')

            for i in range(1, len(lst)):
                if i % 15 == 0:
                    print(lst[i])
                else:
                    print(lst[i], end=', ')
            print()
            print('================================')
            print(f'There are "{len(lst)}" words start with "{letter}"')

        print('================================')

    elif menu_choice == '3':
        # add new word to a file
        with open(filename, 'r') as f:
            lst = []
            for line in f:
                lst.append(line.strip())

        word = input('Enter a word : ')
        while True:
            if word in lst:
                print(f'"{word}" is already in the file')
                word = input('Enter a word : ')
            elif len(word) == 5:
                with open(filename, 'a') as f:
                    # append new word to the file and new row
                    f.write('word + ')
                print(f'"{word}" is added to the file')
                break
            else:
                print('word must be 5 letter')
                word = input('Enter a word : ')


run('sgb-words.txt')
