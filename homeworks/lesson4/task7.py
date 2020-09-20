"""
7. Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def read_not_negative_int():
    while True:
        input_value = input("Введите целое положительное значение n:\n")
        try:
            input_value = int(input_value)
            if input_value < 0:
                print('Введенное значение не является целым положительным числом')
                continue
            return input_value
        except ValueError:
            print('Введенное значение не является целым числом')
            continue


def fact(n: int):
    current_fact = 1
    for x in range(1, n+1):
        current_fact = current_fact * x
        yield current_fact

n = read_not_negative_int()
print(f'Значение от 1! до {n}!')
for el in fact(n):
    print(el)