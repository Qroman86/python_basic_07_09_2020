"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
from typing import List


def read_numbers() -> List:
    """
    Считывает список чисел
    :return: считанный список чисел
    """
    while True:
        input_list = input('Введите числа, разделенные запятой:\n').split(',')
        numbers_list = []
        is_input_correct = True
        for item in input_list:
            try:
                numbers_list.append(float(item))
            except ValueError:
                print('Введенная строка включает нечисла')
                is_input_correct = False
                break
        if not is_input_correct:
            continue

        return numbers_list


def non_repeat_list(input_list: List) -> List:
    """
    Функция возвращающая неповторяющиеся элементы списка в том же порядке
    :param input_list: входной список
    :return: выходной список
    """
    output_list = [x for x in input_list if input_list.count(x) == 1]
    return output_list


assert non_repeat_list([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]) == [23, 1, 3, 10, 4, 11], "Функция non_repeat_list работает неверно"

example_list = read_numbers()
print(f"Для списка {example_list} результат работы функции non_repeat_list будет следующим:\n{non_repeat_list(example_list)}")