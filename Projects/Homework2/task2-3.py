'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

number_of_month = int(input('Введите номер месяца: '))
list_of_months = [
    [12, 1, 2, 'зима'],
    [3, 4, 5, 'весна'],
    [6, 7, 8, 'лето'],
    [9, 10, 11, 'осень']
]

for i in range(len(list_of_months)):
    for j in range(len(list_of_months)):
        if number_of_month in list_of_months[i][0:3]:
            print(list_of_months[i][3])
            break

dict_of_months = {
    'зима': (12, 1, 2),
    'весна': (3, 4, 5),
    'лето': (6, 7, 8),
    'осень': (9, 10, 11)
}

for key, value in dict_of_months.items():
    if number_of_month in value:
        print(key)
