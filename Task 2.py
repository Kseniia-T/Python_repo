"""
Author: Kseniia Tokhtamysheva
Task 2 to Lesson 2:

2)	Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

my_list = list (input('Input a list: '))
i  = 0
for i in range(1, len(my_list), 2):
    my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]
print(''.join([str(i) for i in my_list]))
