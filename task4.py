'''4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.'''

n = input('Введите целое положительное число: ')
count_of_numbers = len(n)
n = int(n)
count = 0
max_number = 0
while count < count_of_numbers:
    x = n % 10
    if x > max_number:
        max_number = x
    n = n // 10
    count += 1

print(max_number)
