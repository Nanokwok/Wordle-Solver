from database import Database
from solver import Solver
import random


def run(filename):  # main function
    # menu
    print('Hello ! welcome to WORDLE SOLVER')
    print('================================')
    print('menu:')
    print('open slover [1]')
    print('display all word in a file [2]')
    print('add new word to a file [3]')
    menu_choice = input('What you selected : ')  # menu choice
    print('================================')
    if menu_choice == '1':  # open slover
        rounds = 1
        DB = Database(filename)  # create a database object
        SOLVER = Solver(DB.read_file(filename))  # create a solver object
        word_lst = DB.read_file(filename)  # read file and store in a list
        word_lst = [i.word for i in word_lst]  # store word in a list
        ans = ['dealt', 'roate', 'store', 'ocean']  # answer list
        lst = []  # list for store word
        while True:
            if rounds == 1:
                print('good starting words to use for Wordle…')
                print('dealt [1]')
                print('roate [2]')
                print('store [3]')
                print('ocean [4]')
                print('((Your own guess)) [5]')
                yes_or_no = input('Have you won? (y/n) : ')
                if yes_or_no == 'y':  # if user win
                    print('Congratulations!')
                    print('================================')
                    print('Do you want to play again?')
                    print('Yes [1]')
                    print('No [2]')
                    play_again = input('What you selected : ')
                    if play_again == '1':  # if user want to play again
                        continue
                    elif play_again == '2':  # if user don't want to play again
                        break
                elif yes_or_no == 'n':  # if user don't win
                    select = input('What you selected : ')
                    while select not in ['1', '2', '3', '4', '5']:
                        print('Invalid input. Please try again.')
                        select = input('What you selected : ')
                    if select != '5':  # if user select a word from the list
                        print(f'You selected "{ans[int(select) - 1]}"')
                        print('================================')
                        g_index = SOLVER.eliminate_g(word_lst, ans[int(select) - 1])  # eliminate green
                        y_index = SOLVER.eliminate_y(word_lst, ans[int(select) - 1])  # eliminate yellow
                        SOLVER.eliminate_b(word_lst, ans[int(select) - 1], g_index, y_index)  # eliminate black
                        lst.append(SOLVER.display_word(ans[int(select) - 1], g_index, y_index))  # display word

                        print('================================')

                    else:
                        own_word = input('Enter your word : ')
                        g_index = SOLVER.eliminate_g(word_lst, own_word)
                        y_index = SOLVER.eliminate_y(word_lst, own_word)
                        SOLVER.eliminate_b(word_lst, own_word, g_index, y_index)
                        lst.append(SOLVER.display_word(own_word, g_index, y_index))

                        print('================================')

                    rounds += 1

                else:
                    print('Please enter y or n')
                    print('================================')

            else:
                print('Suggested words…')
                sug = []  # list for store suggested word
                for i in word_lst:  # loop through word list
                    if i != 'x':
                        sug.append(i)

                rand = []
                if len(sug) > 4: # if there are more than 4 word in the list
                    for i in range(4):
                        random_word = random.choice(sug)  # random a word
                        while random_word in lst:  # if the word is already in the list
                            random_word = random.choice(sug)  # random again
                        rand.append(random_word)
                else:
                    for i in range(len(sug)):  # if there are less than 4 word in the list
                        random_word = random.choice(sug)  # random a word
                        while random_word in lst:
                            random_word = random.choice(sug)
                        rand.append(random_word)

                for i in range(len(rand)):
                    print(f'{rand[i]} [{i + 1}]')  # display suggested word

                print(f'((Your own guess)) [{len(rand) + 1}]')

                ans = rand  # store suggested word in a list

                yes_or_no = input('Have you won? (y/n) : ')
                if yes_or_no == 'y':
                    print('Congratulations!')
                    print('================================')
                    print('Do you want to play again?')
                    print('Yes [1]')
                    print('No [2]')
                    play_again = input('What you selected : ')
                    if play_again == '1':
                        continue
                    elif play_again == '2':
                        break
                elif yes_or_no == 'n':
                    select = input('What you selected : ')
                    while select not in ['1', '2', '3', '4', '5']:  # if user enter invalid input
                        print('Invalid input. Please try again.')
                        select = input('What you selected : ')
                    if int(select) != len(rand) + 1:
                        print(f'You selected "{rand[int(select) - 1]}"')  # display word
                        print('================================')
                        g_index = SOLVER.eliminate_g(word_lst, rand[int(select) - 1])
                        y_index = SOLVER.eliminate_y(word_lst, rand[int(select) - 1])
                        SOLVER.eliminate_b(word_lst, rand[int(select) - 1], g_index, y_index)
                        lst.append(SOLVER.display_word(rand[int(select) - 1], g_index, y_index))

                        print('================================')
                    else:
                        own_word = input('Enter your word : ')
                        if type(own_word) == str:
                            print(f'You selected "{own_word}"')
                            g_index = SOLVER.eliminate_g(word_lst, own_word)
                            y_index = SOLVER.eliminate_y(word_lst, own_word)
                            SOLVER.eliminate_b(word_lst, ans[int(select) - 1], g_index, y_index)
                            lst.append(SOLVER.display_word(own_word, g_index, y_index))

                            print('================================')
                        else:
                            while True:
                                print('Invalid word. Please try again.')
                                own_word = input('Enter your word : ')
                                if all(SOLVER.check_five() and SOLVER.check_real()):
                                    print(f'You selected "{own_word}"')
                                    g_index = SOLVER.eliminate_g(word_lst, own_word)
                                    y_index = SOLVER.eliminate_y(word_lst, own_word)
                                    SOLVER.eliminate_b(word_lst, ans[int(select) - 1], g_index, y_index)
                                    lst.append(SOLVER.display_word(own_word, g_index, y_index))

                                    print('================================')
                                    break
                else:
                    print('Please enter y or n')
                    print('================================')

    elif menu_choice == '2':
        print('display all word in a file [1]')
        print('display just letter word in a file [2]')
        inp = input('What you selected : ')
        print('================================')
        if inp == '1':
            DB = Database(filename)  # create a database object
            lst = DB.read_file(filename)  # read file
            SOLVER = Solver(lst)  # create a solver object
            SOLVER.update()  # update the word list
            lst_ = SOLVER.word_list  # store the word list

            for i in range(1, len(lst_)):  # loop through the word list
                if i % 15 == 0:  # if the word is the 15th word
                    print(lst_[i - 1].word)  # print the word
                else:
                    print(lst_[i - 1].word, end=', ')  # print the word with comma
            print()
            print(f'There are "{len(lst_)}" words in the file')  # display the number of word in the file

        elif inp == '2':
            letter = input('Enter a letter : ')
            with open(filename, 'r') as f:  # open the file
                lst = []  # list for store word
                for line in f:  # loop through the file
                    if line[0] == letter:
                        lst.append(line.strip())

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
        DB = Database(filename)
        lst = DB.read_file(filename)

        word = input('Enter a word : ')  # ask user to enter a word
        while True:
            if word in lst:
                print(f'"{word}" is already in the file')  # if the word is already in the file
                word = input('Enter a word : ')
            elif len(word) == 5:
                DB.add_word(word, filename)  # add the word to the file
                break
            else:
                print('word must be 5 letter')
                word = input('Enter a word : ')


run('sgb-words.txt')  # run the program
