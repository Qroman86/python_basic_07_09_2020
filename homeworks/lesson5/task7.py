from typing import List, Dict
import json
import os


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


def ser_json_to_file(file_name: str, list: List):
    """
    Записать строки в файл
    :param file_name: имя файла
    :param dict: список для сериализации в формате json
    :return:
    """
    if not file_name:
        raise ValueError("Передано пустое значение имени файла")
    try:
        with open(file_name, "w", encoding="UTF-8") as f_obj:
            json.dump(list, f_obj)
    except IOError:
        raise IOError(f"Ошибка ввода-вывода в файл {file_name}!")


def fetch_name_and_income_data(input_str: str, income_dict: Dict):
    """
    Записать в словарь данные о названии фирмы и ее прибыли
    :param input_str: входная строка
    :param income_dict: словарь с данными о названии фирм и их прибыли
    """
    input_str = input_str.replace('\n', '')
    split_result = input_str.split(" ")
    if len(split_result) != 4:
        raise ValueError("Неверный формат строки")
    try:
        profit = float(split_result[3]) - float(split_result[2])
        income_dict.update({split_result[0]:profit})
    except ValueError:
        raise ValueError("Неверный формат строки")


def calculate_average_value(profit_dict: Dict) -> float:
    """
    Расчитать среднее значения прибыли в случае отсутствия убытков
    :param profit_dict: входной словарь с данными по названию фирм и их прибыли
    :return: среднее значение прибыли
    """
    counter = 0
    total_sum = 0.0
    for profit in profit_dict.values():
        if profit < 0:
            continue
        counter += 1
        total_sum += profit
    if counter > 0:
        total_sum /= counter
    return total_sum


def convert_str_list_to_data_list(data_list: List) -> List:
    """
    Конвертировать список строк с данными по фирмам в список, состояший из словаря фирм и
    среднего значения прибыли
    :param data_list: список строк с данными по фирмам
    :return: список, состоящий из словаря фирм и среднего значения прибыли
    """
    result_list = []
    profit_dict = {}
    for data_item in data_list:
        fetch_name_and_income_data(data_item, profit_dict)
    result_list.append(profit_dict)
    result_list.append({"average_profit": calculate_average_value(profit_dict)})
    return result_list


if __name__ == '__main__':
    try:
        file_path_in = os.path.join(os.path.dirname(__file__), 'task7_in.txt')
        str_data_list = read_data_from_file(file_path_in)
        #prepare complex_dict
        data_list = convert_str_list_to_data_list(str_data_list)
        #write json to file
        file_path_out = os.path.join(os.path.dirname(__file__), 'task7_out.txt')
        ser_json_to_file(file_path_out, data_list)
    except IOError:
        print("Внимание! Во время выполнения программы произошла ошибка")
    except ValueError:
        print("Внимание! Во время выполнения программы произошла ошибка")