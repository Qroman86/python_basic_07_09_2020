"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка
описывает учебный предмет и наличие лекционных, практических и лабораторных занятий
по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и
общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
from typing import List, Dict


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


def count_hours_from(input_str: str) -> float:
    """
    Подсчитать общее число часов
    :param input_str: строка с записью чисео
    :return: значение общего числа часов
    """
    total_sum = 0.0
    number = ""
    is_digit = False
    for symbol in input_str:
        if symbol.isdigit():
            is_digit = True
            number += symbol
        else:
            if is_digit:
                try:
                    total_sum += float(number)
                except ValueError:
                    raise ValueError("Неправильный формат строки")
            number = ""
            is_digit = False
    return total_sum


def read_data_from_str(input_str: str):
    """
    Подготовить данные из строки в формате Предмет:строка_с_данными_о_часах
    :param input_str: входная строка
    :return: Название предмета, Общее количество часов
    """
    split_str = input_str.split(":")
    if len(split_str) != 2:
        raise ValueError("Строка не соответствует формату")
    return split_str[0], count_hours_from(split_str[1])


def prepare_subject_dict(str_data_list: List) -> Dict:
    """
    Формирует словарь с данными по предметам на основе введеного списка строк
    :param str_data_list: исходный список строк
    :return: словарь с данными по предметам
    """
    subject_dict = {}
    for raw in str_data_list:
        subject, total_hours_count = read_data_from_str(raw)
        subject_dict.update({subject: total_hours_count})
    return subject_dict


if __name__ == '__main__':
    str_data_list = []
    try:
        str_data_list = read_data_from_file("task6.txt")
    except IOError:
        print("Ошибка чтения из файла")
    except ValueError:
        print("Ошибка чтения из файла")

    try:
        subject_dict = prepare_subject_dict(str_data_list)
    except ValueError:
        print("Ошибка при формировании словаря")
    print(f"Информация по общему количеству часов в разрезе по предметам:\n{subject_dict}")