"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
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

def prepare_list(input_list: List) -> List:
    """
    Создать список элементов из исходного по принципу элемент должен быть
    больше предыдущего
    :param input_list: исходный список
    :return: список-результат
    """
    output_list = [item for id, item in enumerate(input_list) if id > 0 and item > input_list[id-1]]
    return output_list


assert  [12, 44, 4, 10, 78, 123] == prepare_list([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]), "Функция prepare_list работает неверно"

number_list = read_numbers()
print(f"Результат работы функции prepare_list для списка {number_list}:\n {prepare_list(number_list)}")