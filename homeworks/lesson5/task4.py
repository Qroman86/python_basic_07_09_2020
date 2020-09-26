"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
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


def translate_from_en_to_ru(input_str: str) -> str:
    """
    Выполнить перевод для строки с английского на русский
    :param input_str: строка на английском
    :return: строка на русском
    """
    input_split = input_str.split(" — ")
    translate_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    if len(input_split) != 2:
        raise ValueError(f"Неверный формат строки: {input_str}")
    ru_value = translate_dict.get(input_split[0])
    return f"{ru_value} — {input_split[1]}"


def translate_from_en_to_ru_for_raws(str_list: List) -> List:
    """
    Выполнить перевод для списка строк с английского на русский
    :param str_list: список строк на английском
    :return: список строк на русском
    """
    ru_list = []
    for en_raw in str_list:
        ru_raw = translate_from_en_to_ru(en_raw)
        ru_list.append(ru_raw)
    return ru_list


if __name__ == '__main__':
    try:
        file_path_in = os.path.join(os.path.dirname(__file__), 'task4_in.txt')
        str_raws = read_data_from_file(file_path_in)
        str_raws = translate_from_en_to_ru_for_raws(str_raws)
        file_path_out = os.path.join(os.path.dirname(__file__), 'task4_out.txt')
        write_to_file(file_path_out, str_raws)
    except:
        print("\nВнимание! Во время выполнения программы произошла ошибка")