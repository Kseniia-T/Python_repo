"""
Author: Kseniia Tokhtamysheva
Task 3 to Lesson 2:

3)	Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
#через dict

number = int(input('Please input a month number: '))
month_dict = {
    'Winter': (1, 2, 12),
    'Spring': (3, 4, 5),
    'Summer': (6, 7, 8),
    'Autumn': (9, 10, 11)
 }
for key in month_dict.keys():
    if number in month_dict[key]:
        print(key)


#через list
number_new = int(input('Please input a new month number: '))
list_w = [1, 2, 12]
list_sp = [3, 4, 5]
list_sm = [6, 7, 8]
list_at = [9, 10, 11]
if number_new in list_w:
    print('Winter')
elif number_new in list_sp:
    print('Spring')
elif number_new in list_sm:
    print('Summer')
elif number_new in list_at:
    print('Autumn')


