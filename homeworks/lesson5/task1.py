"""1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""
from typing import List


def read_lines_from_user() -> List:
    str_list = []
    print("Вводите построчно строки, по окончанию введите пустую строку:")
    while True:
        input_str = input()
        if not input_str:
            break
        str_list.append(input_str)
    return str_list


def write_to_file(file_name: str, str_list: List):
    if not file_name:
        raise ValueError("Передано пустое значение имени файла")
    try:
        with open(file_name, "w") as f_obj:
            f_obj.writelines("%s\n" % line for line in str_list)
    except IOError:
        raise IOError(f"Ошибка ввода-вывода в файл {file_name}!")


if __name__ == '__main__':
    try:
        file_name_value = input("Введите имя файла:\n")
        write_to_file(file_name_value, read_lines_from_user())
    except:
        print("\nВнимание! Во время выполнения программы произошла ошибка")