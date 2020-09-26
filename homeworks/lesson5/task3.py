"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
import os
from typing import List


def fetch_employee_data_from_raws(raw_data: List):
    """
    Считать данные сотрудников из списка строк
    :param raw_data: список строк
    :return: список данных о сотрудниках (Фамилия, Зарплата)
    """
    employee_list = []
    for raw in raw_data:
        split_data = raw.split(' ')
        if len(split_data) != 2:
            continue
        surname = split_data[0]
        salary = split_data[1]
        try:
            salary = float(salary)
        except ValueError as e:
            raise ValueError(f"В строке для {surname} указано нечисловое значение оклада")
        employee_list.append((surname, salary))
    return employee_list


def prepare_employee_list_less_salary(employee_list: List, salary_level: float) -> List:
    """
    Подготавливает на основе введенного списка сотрудников и заданного уровня з/п
    список сотрудников с меньшим окладом
    :param employee_list: список сотрудников
    :param salary_level: уровень оклада
    :return: список сотрудников с меньшим окладом
    """
    employee_list_less_salary = []
    for employee_data in employee_list:
        if employee_data[1] < salary_level:
            employee_list_less_salary.append(employee_data[0])
    return employee_list_less_salary


def calc_average_salary(employee_list: List) -> float:
    """
    расчет среднего значения оклада
    :param employee_list: список сотрудников
    :return: среднее значение оклада
    """
    total_sum = 0
    if len(employee_list) == 0:
        return 0
    for employee in employee_list:
        total_sum += employee[1]
    return total_sum/len(employee_list)


def print_employee_data_from_file(file_name: str):
    """
    Вывести список сотрудников с зарплатой меньше 20000,
    Ввести среднюю величну дохода сотрудников
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

    employee_list = fetch_employee_data_from_raws(str_raws)

    salary_level = 20000
    employee_list_less_salary = prepare_employee_list_less_salary(employee_list, salary_level)
    print(f"\nСписок сотрудников с окладом менее {salary_level}:")
    for employee in employee_list_less_salary:
        print(employee)

    average_salary = calc_average_salary(employee_list)
    print(f"\nСредняя величина дохода сотрудников равна {average_salary}")


if __name__ == '__main__':
    try:
        file_path = os.path.join(os.path.dirname(__file__), 'task3.txt')
        print_employee_data_from_file(file_path)
    except:
        print("\nВнимание! Во время выполнения программы произошла ошибка")