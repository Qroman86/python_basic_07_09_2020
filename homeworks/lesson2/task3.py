'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''
month_number = 0
while True:
    month_number = input('Введите номер месяца от 1 до 12:\n')
    if month_number.isdigit():
        month_number = int(month_number)
        if month_number >= 1 and month_number <= 12:
            break

season_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
if month_number > 0:
    print(f'Время года (list): {season_list[month_number-1]}')

season_map = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}
print(f'Время года (map): {season_map.get(month_number)}')