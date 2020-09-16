'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''

def sum_up(input_list):
    """
    calculate sum of list of numbers
    :param input_list: list of numbers
    :return: sum of numbers
    """
    is_stop = False
    sum = 0
    for input_item in input_list:
        if input_item == 'q':
            is_stop = True
            break
        try:
            input_number = float(input_item)
            sum += input_number
        except ValueError as error:
            continue
    return is_stop, sum

def ask_numbers(input_str):
    """
    Ask numbers from user
    :param input_str: ask sentence
    :return: None
    """
    total_sum = 0
    while True:
        input_numbers_str = input(input_str)
        input_list = input_numbers_str.split(" ")
        is_stop, sum = sum_up(input_list)
        total_sum += sum
        print(f"Текущее значение суммы чисел равно:{total_sum}")
        if is_stop:
            break


ask_numbers("\nВведите строку чисел, разделенных пробелом (для остановки программы укажите в строке 'q'\n")