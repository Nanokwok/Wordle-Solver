from database import Database
# from word import Word
from solver import Solver
import random



# list_obj = []
# with open('sgb-words.txt') as f:
#     word = f.read().splitlines()
#     list_obj.append(Word(word))


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
        # rounds = 1
        # DB = Database(filename)
        # word_lst = DB.read_file(filename)
        # # word_lst = Database.read_file(filename)
        # # with open(filename, 'r') as f:
        # #     word_lst = []
        # #     for line in f:
        # #         word_lst.append(line.strip())
        # SOLVER = Solver(word_lst)
        #
        # # if rounds == 1:
        # rounds = 1
        # ans = ['dealt', 'roate', 'store', 'ocean']
        # print('good starting words to use for Wordle…')
        # print('dealt [1]')
        # print('roate [2]')
        # print('store [3]')
        # print('ocean [4]')
        # print('((Your own guess)) [5]')
        # yes_or_no = input('Have you won? (y/n) : ')
        # if yes_or_no == 'y':
        #     print('Congratulations!')
        # elif yes_or_no == 'n':
        #     while True:
        #         if rounds == 1:
        #             pass
        #         elif rounds > 1:
        #             yes_or_no = input('Have you won? (y/n) : ')
        #         select = input('What you selected : ')
        #         print(f'You selected "{ans[int(select) - 1]}"')
        #         # Solver.eliminate_g(word_lst, ans[int(select) - 1])
        #         # Solver.eliminate_y(word_lst, ans[int(select) - 1])
        #         # Solver.display_word(ans[int(select) - 1], g_index, y_index)
        #         g_index = SOLVER.eliminate_g(word_lst, ans[int(select) - 1])
        #         y_index = SOLVER.eliminate_y(word_lst, ans[int(select) - 1])
        #         SOLVER.display_word(ans[int(select) - 1], g_index, y_index)
        #         print('================================')
        #         print('Suggested words…')
        #         sug = []
        #         for i in word_lst:
        #             if i != 'x':
        #                 sug.append(i)
        #
        #         rand = []
        #         if len(sug) > 4:
        #             for i in range(4):
        #                 rand.append(random.choice(sug))
        #         else:
        #             for i in range(len(sug)):
        #                 rand.append(random.choice(sug))
        #
        #         for i in range(len(rand)):
        #             print(f'{rand[i]} [{i + 1}]')
        #
        #         print(f'((Your own guess)) [{len(rand) + 1}]')
        rounds = 1
        DB = Database(filename)
        SOLVER = Solver(DB.read_file(filename))
        word_lst = DB.read_file(filename)
        word_lst = [i.word for i in word_lst]
        ans = ['dealt', 'roate', 'store', 'ocean']
        lst = []
        # word_lst = SOLVER.word_lst

        # dump_g = []
        # dump_y = []
        while True:
            if rounds == 1:
                print('good starting words to use for Wordle…')
                print('dealt [1]')
                print('roate [2]')
                print('store [3]')
                print('ocean [4]')
                print('((Your own guess)) [5]')
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
                    while select not in ['1', '2', '3', '4', '5']:
                        print('Invalid input. Please try again.')
                        select = input('What you selected : ')
                    if select != '5':
                        print(f'You selected "{ans[int(select) - 1]}"')
                        print('================================')
                        # Solver.eliminate_g(word_lst, ans[int(select) - 1])
                        # Solver.eliminate_y(word_lst, ans[int(select) - 1])
                        # Solver.display_word(ans[int(select) - 1], g_index, y_index)
                        g_index = SOLVER.eliminate_g(word_lst, ans[int(select) - 1])
                        y_index = SOLVER.eliminate_y(word_lst, ans[int(select) - 1])
                        SOLVER.eliminate_b(word_lst, ans[int(select) - 1], g_index, y_index)
                        # SOLVER.display_word(ans[int(select) - 1], g_index, y_index)
                        lst.append(SOLVER.display_word(ans[int(select) - 1], g_index, y_index))
                        # print(lst)
                        # SOLVER.update_word_lst(word_lst)
                        # dump_g.append(g_index)
                        # dump_y.append(y_index)
                        print('================================')

                    else:
                        own_word = input('Enter your word : ')
                        g_index = SOLVER.eliminate_g(word_lst, own_word)
                        y_index = SOLVER.eliminate_y(word_lst, own_word)
                        SOLVER.eliminate_b(word_lst, own_word, g_index, y_index)
                        # SOLVER.display_word(own_word, g_index, y_index)
                        lst.append(SOLVER.display_word(own_word, g_index, y_index))
                        # print(lst)
                        # SOLVER.update_word_lst(word_lst)
                        # dump_g.append(g_index)
                        # dump_y.append(y_index)

                        print('================================')

                    rounds += 1

                else:
                    print('Please enter y or n')
                    print('================================')


            else:
                print('Suggested words…')
                sug = []
                for i in word_lst:
                    if i != 'x':
                        sug.append(i)

                rand = []
                if len(sug) > 4:
                    for i in range(4):
                        random_word = random.choice(sug)
                        while random_word in lst:
                            random_word = random.choice(sug)
                        rand.append(random_word)
                else:
                    for i in range(len(sug)):
                        random_word = random.choice(sug)
                        while random_word in lst:
                            random_word = random.choice(sug)
                        rand.append(random_word)

                for i in range(len(rand)):
                    print(f'{rand[i]} [{i + 1}]')

                print(f'((Your own guess)) [{len(rand) + 1}]')

                ans = rand

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
                    while select not in ['1', '2', '3', '4', '5']:
                        print('Invalid input. Please try again.')
                        select = input('What you selected : ')
                    if int(select) != len(rand) + 1:
                        print(f'You selected "{rand[int(select) - 1]}"')
                        print('================================')
                        g_index = SOLVER.eliminate_g(word_lst, rand[int(select) - 1])
                        y_index = SOLVER.eliminate_y(word_lst, rand[int(select) - 1])
                        SOLVER.eliminate_b(word_lst, rand[int(select) - 1], g_index, y_index)
                        # SOLVER.display_word(rand[int(select) - 1], g_index, y_index)
                        lst.append(SOLVER.display_word(rand[int(select) - 1], g_index, y_index))
                        # print(lst)
                        # SOLVER.update_word_lst(word_lst)
                        # dump_g.append(g_index)
                        # dump_y.append(y_index)

                        print('================================')
                    else:
                        own_word = input('Enter your word : ')
                        if type(own_word) == str:
                            print(f'You selected "{own_word}"')
                            g_index = SOLVER.eliminate_g(word_lst, own_word)
                            y_index = SOLVER.eliminate_y(word_lst, own_word)
                            SOLVER.eliminate_b(word_lst, ans[int(select) - 1], g_index, y_index)
                            # SOLVER.display_word(own_word, g_index, y_index)
                            lst.append(SOLVER.display_word(own_word, g_index, y_index))
                            # print(lst)
                            # SOLVER.update_word_lst(word_lst)
                            # dump_g.append(g_index)
                            # dump_y.append(y_index)

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
                                    # SOLVER.display_word(own_word, g_index, y_index)
                                    lst.append(SOLVER.display_word(own_word, g_index, y_index))
                                    # print(lst)
                                    # SOLVER.update_word_lst(word_lst)
                                    # dump_g.append(g_index)
                                    # dump_y.append(y_index)

                                    print('================================')
                                    # print(word_lst)
                                    break
                else:
                    print('Please enter y or n')
                    print('================================')

    elif menu_choice == '2':
        # display all word in a file
        print('display all word in a file [1]')
        print('display just letter word in a file [2]')
        inp = input('What you selected : ')
        print('================================')
        if inp == '1':
            # with open(filename, 'r') as f:
            #     lst = []
            #     for line in f:
            #         lst.append(line.strip())
            DB = Database(filename)
            lst = DB.read_file(filename)
            SOLVER = Solver(lst)
            SOLVER.update()
            # word_class_list = []

            # for i in SOLVER._word_lst:
            #     word_class_list.append(Word(i))
            lst_ = SOLVER.word_list
            # lst = Database.read_file('sgb-words.txt')

            for i in range(1, len(lst_)):
                if i % 15 == 0:
                    print(lst_[i - 1].word)
                else:
                    print(lst_[i - 1].word, end=', ')
            print()
            print(f'There are "{len(lst_)}" words in the file')

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
        DB = Database(filename)
        lst = DB.read_file(filename)

        word = input('Enter a word : ')
        while True:
            if word in lst:
                print(f'"{word}" is already in the file')
                word = input('Enter a word : ')
            elif len(word) == 5:
                # with open(filename, 'a') as f:
                #     # append new word to the file and new row
                #     f.write('word + ')
                # print(f'"{word}" is added to the file')
                DB.add_word(word)
                break
            else:
                print('word must be 5 letter')
                word = input('Enter a word : ')


run('sgb-words.txt')
