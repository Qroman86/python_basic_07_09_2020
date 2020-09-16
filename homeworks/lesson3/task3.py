"""
    3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
    и возвращает сумму наибольших двух аргументов.
"""
def ask_number(input_str):
    """
        Ask number from user
        :param input_str: str ask sentence
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

def my_func(first_arg: float, second_arg: float, third_arg: float):
    """
    Calculate sum of two maximum values from these three input values
    :param first_arg: first value
    :param second_arg: second value
    :param third_arg: third value
    :return: result of sum
    """
    if first_arg <= second_arg and first_arg <= third_arg:
        return second_arg + third_arg
    elif second_arg <= third_arg:
        return first_arg + third_arg
    else:
        return first_arg + second_arg


first_number = ask_number("Введите первое число:\n")
second_number = ask_number("Введите второе число:\n")
third_number = ask_number("Введите третье число:\n")

sum_of_two_max = my_func(second_arg=second_number, first_arg=first_number, third_arg=third_number)
print(f"Сумма двух наибольших аргументов равна {sum_of_two_max}")
