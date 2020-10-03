"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


def read_float_from_user(input_str: str):
    while True:
        try:
            return float(input(input_str))
        except ValueError as e:
            print("Было введено нечисло")
            continue


if __name__  == '__main__':

    numerator = read_float_from_user("Введите числитель:\n")
    denumerator = read_float_from_user("Введите знаменатель:\n")
    if denumerator == 0:
        raise MyZeroDivisionError("В качестве знаменателя был указан 0, что недопустимо")
    ratio = numerator / denumerator
    print(ratio)
