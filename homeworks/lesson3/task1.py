"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def ask_number(input_str):
    """
    Ask number from user
    :param input_str: ask sentence
    :return: float number
    """
    while True:
        input_number = input(input_str)
        try:
            input_number = float(input_number)
        except ValueError as error:
            print("Необходимо ввести числовое значение")
            continue
        return input_number


def divide(dividend, divider):
    """
    Calculate division
    :param dividend: float value of dividend
    :param divider: float value of divider
    :return: float result of division
    """
    try:
        div_result = dividend / divider;
        return div_result
    except ZeroDivisionError:
        print("Нельзя делить на ноль")


dividend = ask_number("Введите делимое:\n")
divider = ask_number("Введите делитель:\n")

div_result = divide(dividend, divider)
if div_result is not None:
    print(f"{div_result}")
