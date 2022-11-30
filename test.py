# # x = '123'
# #
# # y = [i for i in x]
# # print(y)
#
with open('sgb-words.txt') as f:
    word = f.read().splitlines()
    print(word)
#
# ans = 'water'
#
#
# def eliminate_g():
#     num = ['1', '2', '3', '4', '5', '-']
#     green = input('Input green tile index(es) (if not input -) : ')
#     index = [i for i in green]
#
#     bool = all(i in num for i in index)
#
#     while not bool:
#         print('Invalid input')
#         green = input('Input green tile index(es) (if not input -) : ')
#         index = [i for i in green]
#         bool = all(i in num for i in index)
#
#     if green != '-':
#         for i in range(len(index)):
#             index[i] = int(index[i])
#
#     if green == '-':
#         pass
#     else:
#         letter_correct = []
#         for i in index:
#             letter_correct.append(ans[i - 1])
#
#         for i in range(len(lst)):
#             for j in range(len(letter_correct)):
#                 if letter_correct[j] not in lst[i]:
#                     lst[i] = 'x'
#                 elif lst[i][index[j] - 1:index[j]] != letter_correct[j]:
#                     lst[i] = 'x'
#     return lst, index
#
#
# def eliminate_y():
#     num = ['1', '2', '3', '4', '5', '-']
#     yellow = input('Input yellow tile index(es) (if not input -) : ')
#     index = [i for i in yellow]
#
#     bool = all(i in num for i in index)
#
#     while not bool:
#         print('Invalid input')
#         yellow = input('Input yellow tile index(es) (if not input -) : ')
#         index = [i for i in yellow]
#         bool = all(i in num for i in index)
#
#     if yellow != '-':
#         for i in range(len(index)):
#             index[i] = int(index[i])
#
#     if yellow == '-':
#         pass
#     else:
#         letter_correct = []
#         for i in index:
#             letter_correct.append(ans[i - 1])
#
#         for i in range(len(lst)):
#             for j in range(len(letter_correct)):
#                 if lst[i] == 'x':
#                     pass
#                 elif letter_correct[j] not in lst[i]:
#                     lst[i] = 'x'
#                 elif lst[i][index[j] - 1:index[j]] == letter_correct[j]:
#                     lst[i] = 'x'
#
#     return lst, index
#
#
# # eliminate_g()
# # eliminate_y()
# g_lst, g_index = eliminate_g()
# y_lst, y_index = eliminate_y()
#
# for i in range(1, 6):
#     if i in g_index:
#         print(f"'{(ans[i - 1:i]).upper()}'", end=' ')
#     elif i in y_index:
#         print((ans[i - 1:i]).upper(), end=' ')
#     else:
#         print(ans[i - 1:i], end=' ')
# print()
#
# for i in lst:
#     if i != 'x':
#         print(i)
#
# from word import Word
#
# lst_of_object = []
# for i in lst:
#     lst_of_object.append(Word(i))
#
# print(lst_of_object)
#
# for i in lst_of_object:
#     print(i)
