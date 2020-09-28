"""1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""
import os
from typing import List


def read_lines_from_user() -> List:
    """
    Считать данные пользователя построчно
    :return: список введенных строк, за исключением последней пустой строки
    """
    str_list = []
    print("Вводите построчно строки, по окончанию введите пустую строку:")
    while True:
        input_str = input()
        if not input_str:
            break
        str_list.append(input_str)
    return str_list


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
            f_obj.writelines("%s\n" % line for line in str_list)
    except IOError:
        raise IOError(f"Ошибка ввода-вывода в файл {file_name}!")


if __name__ == '__main__':
    try:
        file_path = os.path.join(os.path.dirname(__file__), 'task1.txt')
        write_to_file(file_path, read_lines_from_user())
    except:
        print("\nВнимание! Во время выполнения программы произошла ошибка")