'''2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите
в формате чч:мм:сс. Используйте форматирование строк.'''

time_in_seconds = int(input('Введите время в секундах: '))
hours = str(time_in_seconds // 3600)
if len(hours) == 1:
    hours = '0'+hours
minutes = str((time_in_seconds % 3600) // 60)
if len(minutes) == 1:
    minutes = '0'+minutes
seconds = str((time_in_seconds % 3600) % 60)
if len(seconds) == 1:
    seconds = '0'+seconds
print(f'{hours}:{minutes}:{seconds}')
