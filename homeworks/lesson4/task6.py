"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle


def read_int(input_str: str) -> int:
    """
    Считать целое число у пользователя
    :param input_str: строка с текстом запроса
    :return: целое число
    """
    while True:
        input_value = input(input_str)
        try:
            input_value = int(input_value)
            return input_value
        except ValueError:
            print('Введенное значение не является целым числом')
            continue


def read_not_negative_int(input_str: str) -> int:
    """
    Считать целое неотрицательное число у пользователя
    :param input_str: строка с текстом запроса
    :return: целое неотрицательное число
    """
    while True:
        int_value = read_int(input_str)
        if int_value < 0:
            print('Введенное значение не должно быть отрицательным')
        return int_value

start_value = read_int('Введите стартовое значения для итератора а) в виде целого числа:\n')
stop_value = read_int('Введите стоп-значение для итератора а) в виде целого числа:\n')

print("\nВывод значений итератора, генерирующего целые числа:")
for el in count(start_value):
    if el > stop_value:
        break
    print(el)

input_list = input('Введите строку, состоящую из элементов, разделенных проблеом:\n').split(' ')
cycle_number = read_not_negative_int("Введите целое неотрицательное число циклов повторений:\n")
cycle_size = len(input_list)
iter_count_max = cycle_size * cycle_number
iter_counter = 0
for el in cycle(input_list):
    if iter_counter >= iter_count_max:
        break
    if iter_counter % cycle_size == 0:
        print(f"Цикл номер {(iter_counter // cycle_size) + 1}")

    print(el)
    iter_counter += 1