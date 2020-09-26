"""
5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import os
from typing import List


def write_to_file(file_name: str, str_list: List):
    """
    Записать строки в файл
    :param file_name: имя файла
    :param str_list: список строк для записи
    :return:
    """
    if not file_name:
        raise ValueError("Передано пустое значение имени файла")
    try:
        with open(file_name, "w", encoding="UTF-8") as f_obj:
            f_obj.writelines("%s" % line for line in str_list)
    except IOError:
        raise IOError(f"Ошибка ввода-вывода в файл {file_name}!")


def read_data_from_file(file_name: str) -> List:
    """
    Считать данные из файла в виде списка строк
    :param file_name: имя файла
    :return: список строк
    """
    str_raws = []
    if not file_name:
        raise ValueError("Передано пустое значение имени файла")
    try:
        with open(file_name, "r", encoding="UTF-8") as f_obj:
            str_raws = f_obj.readlines()
    except IOError:
        raise IOError(f"Ошибка ввода-вывода в файл {file_name}!")
    return str_raws


def read_numbers_from_user() -> List:
    """
    Считать строку чисел
    :return: список чисел в формате строки
    """
    float_list = []

    while True:
        input_str = input("Введите строку из числа, разделенных пробелом:\n")
        numlist_str = input_str.split(" ")
        is_continue = False
        for number in numlist_str:
            try:
                number_val = float(number)
                float_list.append(number)
            except ValueError:
                is_continue = True
                float_list = []
                break
        if not is_continue:
            break
    return float_list


def calculate_sum(input_str: str) -> float:
    """
    Подсчитать сумму чисел в строке, разделенных пробелом
    :param input_str: исходная строка
    :return: сумма чисел
    """
    if not input_str:
        raise ValueError("Пустая строка")
    total_sum = 0.0
    for part_of_str in input_str.split(" "):
        try:
            total_sum += float(part_of_str)
        except ValueError:
            raise ValueError("Строка содержит нечисла")
    return total_sum

if __name__ == '__main__':
    float_list_as_str = read_numbers_from_user()
    float_list_str = " ".join(float_list_as_str)
    file_name = os.path.join(os.path.dirname(__file__), 'task5.txt')

    number_list = []
    try:
        write_to_file(file_name, [float_list_str])
        number_list = read_data_from_file(file_name)
    except IOError:
        print(f"Ошибка чтения/записи для файла {file_name}")
    except ValueError:
        print(f"Ошибка чтения/записи для файла {file_name}")

    if(len(number_list) > 0):
        #считываем из первой строки
        try:
            total_sum = calculate_sum(number_list[0])
            print(f"Сумма чисел в файле (из первой строки) равна {total_sum}")
        except ValueError as error:
            print("Первая строка файла не соответствует требуемому формату")