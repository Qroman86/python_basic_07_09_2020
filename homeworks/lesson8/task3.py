from typing import List
class CheckNumberListError(Exception):
    def __init__(self, txt):
        self.txt = txt


class NumberList:
    @staticmethod
    def read_list_from_user():
        input_list = []
        while True:
            next_element = input("Введите следующий элемент списка, для остановки введите 'stop':\n")
            if next_element == 'stop':
                break
            input_list.append(next_element)
        return input_list

    @staticmethod
    def check_list_for_not_numbers(element_list: List):
        for index, element in enumerate(element_list):
            try:
                element_list[index] = float(element)
            except ValueError:
                raise CheckNumberListError("Список содержит нечисла")


if __name__  == '__main__':
    try:
        input_list = NumberList.read_list_from_user()
        NumberList.check_list_for_not_numbers(input_list)
        print(input_list)
    except CheckNumberListError as e:
        print(e)

