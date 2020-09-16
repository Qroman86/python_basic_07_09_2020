"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

def ask_number(input_str: str, is_real: bool, is_positive: bool):
    """
    Ask number from user
    :param input_str: ask sentence
    :param is_real: is input number should be real
    :param is_positive: is input number should be greater than zero
    :return: value of user number
    """
    is_positive_str = "положительным" if is_positive else "отрицательным"
    is_real_str = "действительным" if is_real else "целым"
    message_str = f"Введенное значение должно быть {is_real_str} {is_positive_str} числом"
    while True:
        input_number = input(input_str)
        try:
            if is_real:
                input_number = float(input_number)
            else:
                input_number = int(input_number)
        except ValueError as error:
            print(message_str)
            continue

        if input_number == 0 or (input_number < 0 and is_positive) or (input_number > 0 and not is_positive):
            print(message_str)
            continue

        return input_number

x = ask_number("\nВведите действительное положительное число x:\n", True, True)
y = ask_number("\nВведите целое отрицательное число y:\n", False, False)

#Первый способ
def my_func1(x: float, y: int):
    """
    Calculate power x**y using '**'
    :param x: x-value
    :param y: y-value
    :return: power value
    """
    return x**y

#Второй способ
def my_func2(x: float, y: int):
    """
        Calculate power x**y using 'while'
        :param x: x-value
        :param y: y-value
        :return: power value
        """
    result = 1.0
    while y < 0:
        result /= x
        y += 1
    return result

print(f"Первый способ:\n{my_func1(x,y)}")
print(f"Второй способ:\n{my_func2(x,y)}")