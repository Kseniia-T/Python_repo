"""
Author: Kseniia Tokhtamysheva
Task 4 to Lesson 2:

4)	Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

my_str = input('Input several words, splitted by gaps: ')
list = my_str.split()
i = 1
for el in list:
    print(f'{i}) {el[0:10]}')
    i += 1


