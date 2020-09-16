"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""

def int_func(word: str):
    """
    Make word as title (uppercase first letter)
    :param word: input word
    :return: result
    """
    uppercase_map = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'h': 'H', 'i': 'I', 'j': 'J'}
    uppercase_map.update({ 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O'})
    uppercase_map.update({'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'})

    if not isinstance(word, str):
        print("Введенное значение пусто или не является строкой")
        return word

    if not word:
        return word

    first_letter = word[0]
    if first_letter not in uppercase_map.keys():
        return word

    first_letter = uppercase_map.get(first_letter)
    if len(word) == 1:
        word = first_letter
    elif len(word) > 1:
        word = first_letter + word[1:]

    return word

def ask_words(input_value):
    """
    Print all word in string as title in one string
    :param input_value: input string
    :return: result string
    """
    if not isinstance(input_value, str):
        print("Введенное значение не является строкой")
        return

    if not input_value:
        print(f"Результирующая строка:'{input_value}'")
        return

    input_words = input_value.split(" ")

    if len(input_words) == 0:
        print(f"Результирующая строка:'{input_value}'")
        return

    word_list = []
    for word in input_words:
        word_list.append(int_func(word))
    output_str = ' '.join(word_list)
    print(f"Результирующая строка:'{output_str}'")

word = input("Введите слово из маленьких латинских буквы:\n")
print(f"Результат работы функции int_func: {int_func(word)}")

words = input("Введите строку из слов из маленьких латинских букв, разделенных пробелом:\n")
ask_words(words)

