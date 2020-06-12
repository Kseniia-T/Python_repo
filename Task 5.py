"""
Author: Kseniia Tokhtamysheva
Task 5 to Lesson 2:

5)	Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен
разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]
new_el = int(input('Please input new rating value: '))

for index in range(len(my_list)):           # Second way:
    if  new_el in my_list:                  # if my_list[el] == new_el:
        index = my_list.index(new_el)       # my_list.insert(el + 1, new_el)
        my_list.insert(index, new_el)
        break
    else:
        my_list.append(new_el)
        my_list.sort(reverse=True)
        break
print(my_list)
