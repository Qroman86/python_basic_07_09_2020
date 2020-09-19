"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def calc_salary(production_in_hours: float, rate_per_hour: float, premium: float) -> float:
    """
    Расчет заработной платы
    :param production_in_hours: выработка в часах
    :param rate_per_hour: ставка в час
    :param premium: размер премии
    :return: размер вычисленной заработной платы
    """
    return production_in_hours*rate_per_hour + premium


def check_float(input_value):
    """
     Проверка является ли введенной значение числом (в случае успеха преобразовать в float)
    :param input_value: входящее значение
    :return: check - True/False (число/нечисло), output_value - преобразованное число (в случае неуспеха None)
    """
    check = False
    output_value = None
    try:
        output_value = float(input_value)
        check = True
    except ValueError as e:
        check = False
    return check, output_value


def define_salary():
    """
        Реализация логики считывания информации из параметров и
        расчет заработной платы.
        Осуществляется проверка на соответствие неотрицитальному значению для
        указанных пользователем выработки в часах, ставки в час и размера премии
    :return: None
    """
    _, production_in_hours, rate_per_hour, premium = argv

    assert calc_salary(10, 10, 10) == 110, "Неверный расчет зарплаты"

    check_as_float, production_in_hours = check_float(production_in_hours)
    if not check_as_float or production_in_hours < 0:
        print("Расчет зарплаты не выполнен! Значение заработной платы должны быть неотрицательным числом")
        return

    check_as_float, rate_per_hour = check_float(rate_per_hour)
    if not check_as_float or rate_per_hour < 0:
        print("Расчет зарплаты не выполнен! Значение ставки в час должно быть неотрицательным числом")
        return

    check_as_float, premium = check_float(premium)
    if not check_as_float or premium < 0:
        print("Расчет зарплаты не выполнен! Значение премии должно быть неотрицательным числом")
        return

    salary = calc_salary(production_in_hours, rate_per_hour, premium)

    print(f"Размер заработной платы равен {salary}")


define_salary()
