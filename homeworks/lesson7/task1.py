from typing import List


class Matrix:
    def __init__(self, matrix_list:List, *args):
        self.__matrix_values = []

        if not isinstance(matrix_list, list):
            raise ValueError("Первым аргументом передан не список")
        if len(matrix_list) == 0:
            raise ValueError("Список списков пуст")

        len_of_rows = 0
        for row_list in matrix_list:
            if not isinstance(row_list, list):
                raise ValueError("В список включен элемент, не являющийся списком")
            if len(row_list) == 0:
                raise ValueError("Вложенный список пуст")
            if len_of_rows > 0 and len_of_rows != len(row_list):
                raise ValueError("Длина вложенных списков неодинакова")
            elif len_of_rows == 0:
                len_of_rows = len(row_list)

            for element_value in row_list:
                if not isinstance(element_value, float) and not isinstance(element_value, int):
                    raise ValueError("Вложенный список содержит нечисло")
            self.__matrix_values.append(row_list)

    @property
    def x_size(self):
        if len(self.__matrix_values) == 0:
            return 0
        return len(self.__matrix_values)

    @property
    def y_size(self):
        return len(self.__matrix_values[0])

    def __str__(self):
        result_str = ""
        for row in self.__matrix_values:
            result_str += ' '.join(str(x) for x in row)+"\n"
        return result_str

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Второй операнд не является экземпаляром класса Matrix")
        if self.x_size != other.x_size:
            raise ValueError("Количество столбцов у складываемых матриц неравно")
        if self.y_size != other.y_size:
            raise ValueError("Количество строк у складываемых матриц неравно")

        sum_list = [[self[x][y] + other[x][y] for y in range(self.y_size)] for x in range(self.x_size)]
        return Matrix(sum_list)

    def __getitem__(self, index):
        return self.__matrix_values[index]



if __name__ == '__main__':
    m1 = Matrix([[1, 2, 2], [3, 4, -3]])
    print(f"Матрица m1:\n{m1}")
    m2 = Matrix([[2, 3, 4], [1, -1, 2]])
    print(f"\nМатрица m2:\n{m2}")
    m3 = m1 + m2
    print(f"\nМатрица m3:\n{m3}")
