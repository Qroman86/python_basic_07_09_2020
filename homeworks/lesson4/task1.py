"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

def calc_salary(production_in_hours: float, rate_per_hour: float, premium: float):
    return production_in_hours*rate_per_hour + premium

def check_float(input_value):
    check = False
    output_value = None
    try:
        output_value = float(input_value)
        check = True
    except ValueError as e:
        check = False
    return check, output_value


_, production_in_hours, rate_per_hour, premium = argv

assert calc_salary(10, 10, 10) == 110, "Неверный расчет зарплаты"

check_as_float, production_in_hours = check_float(production_in_hours)
assert  check_as_float, "Значение заработной платы должны быть неотрицательным числом"
assert  production_in_hours >= 0, "Значение заработной платы должны быть неотрицательным числом"

check_as_float, rate_per_hour = check_float(rate_per_hour)
assert  check_as_float, "Значение ставки в час должно быть неотрицательным числом"
assert  rate_per_hour >= 0, "Значение ставки в час должно быть неотрицательным числом"

check_as_float, premium = check_float(premium)
assert  check_as_float, "Значение премии должно быть неотрицательным числом"
assert  premium >= 0, "Значение премии должно быть неотрицательным числом"

salary = calc_salary(production_in_hours, rate_per_hour, premium)

print(f"Размер заработной платы равен {salary}")