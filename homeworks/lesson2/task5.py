'''
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
'''
number_list = [7, 5, 3, 3, 2]
while True:
    number = input('Введите номер:\n')
    if number.isdigit():
        number = int(number)
    else:
        continue
    if len(number_list) < 1:
        number_list.append(number)
    else:
        index = 0
        while index < len(number_list):
            if number_list[index] < number:
                number_list.insert(index, number)
                break
            if index == len(number_list) - 1:
                number_list.append(number)
                break
            index += 1

    print(f"number_list: {number_list}")

