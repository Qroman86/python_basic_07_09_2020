'''
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''
elements_list = [2, 2.657, 'Это строка', None, [1, 3, 4], (3, 5, 6), {4, 5, 7}, True, b'text', {'key_1': 'val_1', 4: 6, 'some': [5, 6, 4]}, False]

for index, element in enumerate(elements_list):
    element_type = type(element)
    print(f"Type of elements_list[{index}] is {element_type}")

