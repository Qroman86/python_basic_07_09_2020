'''
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''
elements_list = []

# Заполнение списка
while True:
    element = input('Введите элемент (для окончания ввода введите строку "stop":\n')
    if "stop" == element:
        break
    elements_list.append(element)

print(f"elements_list before permutation: {elements_list}")
list_length = len(elements_list)
is_length_odd = True if list_length % 2 == 1 else False
print(f"list_length = {list_length} is_length_odd: {is_length_odd}")

# Перестановка элементов
if list_length > 1:
    current_index = 0
    while current_index < list_length:
        if is_length_odd and current_index == (list_length - 1):
            break
        second_el = elements_list.pop(current_index + 1)
        elements_list.insert(current_index, second_el)
        current_index += 2

print(f"\nelements_list after permutation: {elements_list}")
