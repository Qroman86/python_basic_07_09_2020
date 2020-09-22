"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
from typing import List, Dict


def count_words_in_raws(input_raws: List) -> Dict:
    """
    Подсчитывает количество слов в строках
    :param input_raws: список строк
    :return: словарь с количеством слов для каждого номера строки
    """
    if len(input_raws) == 0:
        return {}
    count_words_data = {}
    for num, input_raw in enumerate(input_raws, 1):
        words_counter = count_words_in_single_raw(input_raw)
        count_words_data.update({num: words_counter})
    return count_words_data


def count_words_in_single_raw(input_str: str) -> int:
    """
    Подсчитывает количество слов в одной строке
    :param input_str: искомая строка
    :return: количество слов
    """
    if not input_str:
        return 0
    input_str = input_str.replace('\n', '')
    if len(input_str) == 0:
        return 0
    return len(input_str.split(' '))


def count_raws_from_file(file_name: str):
    """
    Для указанного имени файла вывести количество слов для каждой строки
    :param file_name: имя файла
    :return:
    """
    str_raws = []
    if not file_name:
        raise ValueError("Передано пустое значение имени файла")
    try:
        with open(file_name, "r", encoding="UTF-8") as f_obj:
            str_raws = f_obj.readlines()
    except IOError:
        raise IOError(f"Ошибка ввода-вывода в файл {file_name}!")
    raws_dict = count_words_in_raws(str_raws)
    print(f"Количество строк {len(raws_dict.keys())}")
    for i in range(1, len(raws_dict.keys())+1):
        print(f"В строке №{i} количество слов равно {raws_dict.get(i)}")


if __name__ == '__main__':
    try:
        file_name_value = "task2.txt"
        count_raws_from_file(file_name_value)
    except:
        print("\nВнимание! Во время выполнения программы произошла ошибка")