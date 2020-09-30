class Cell:
    def __init__(self, cell_number: int, *args):
        if not isinstance(cell_number, int):
            raise ValueError("Введенное значение количества ячеек не является числом")
        if cell_number < 1:
            raise ValueError("Введенное значение количества ячеек не является целым положительным числом")
        self.__cell_number = cell_number

    @property
    def cell_number(self):
        return self.__cell_number

    def __str__(self):
        return f"Количество клеток: {self.__cell_number}"

    def __add__(self, other):
        if not isinstance(other, Cell):
            raise ValueError("Второй операнд не является экземпаляром класса Cell")
        return Cell(self.cell_number + other.cell_number)

    def __sub__(self, other):
        if not isinstance(other, Cell):
            raise ValueError("Второй операнд не является экземпаляром класса Cell")
        if self.cell_number < other.cell_number:
            raise ValueError("Значение первого операнда не может быть меньше значение второго операнда для операции вычитания")
        return Cell(self.cell_number - other.cell_number)

    def __mul__(self, other):
        return Cell(self.cell_number * other.cell_number)

    def __truediv__(self, other):
        if other.cell_number == 0:
            raise ValueError("Деление на ноль запрещено")
        return Cell(self.cell_number // other.cell_number)

    def make_order(cell, cell_row_count: int):
        if not isinstance(cell, Cell):
            raise ValueError("Переданный аргумент cell экземпаляром класса Cell")
        if not isinstance(cell_row_count, int):
            raise ValueError("Переданный аргумент cell_row_count не является целым числом")
        if cell_row_count < 1:
            raise ValueError("Переданный аргумент cell_row_count не является целым положительным числом")
        last_row_len = cell.cell_number % cell_row_count
        number_of_full_rows = cell.cell_number // cell_row_count
        if number_of_full_rows == 0:
            return "*"*last_row_len
        if  number_of_full_rows == 1:
            make_order_str = "*"*cell_row_count
        else:
            make_order_str = ''.join("*"*cell_row_count+"\n" if x < number_of_full_rows - 1 else "*"*cell_row_count  for x in range(number_of_full_rows))
        if last_row_len > 0:
            make_order_str = make_order_str + "\n" + "*"*last_row_len
        return make_order_str
#        ' '.join(str(x) for x in row) + "\n"
 #       sum_list = [[self[x][y] + other[x][y] for y in range(self.y_size)] for x in range(self.x_size)]

if __name__ == '__main__':
    c1 = Cell(7)
    c2 = Cell(3)
    print(f"c1 + c2 = {c1 + c2}")
    print(f"c1 - c2 = {c1 - c2}")
    print(f"c1 / c2 = {c1 / c2}")
    print(f"c1 * c2 = {c1 * c2}")
    print(f"c1 * c2:\n{Cell.make_order(c1 * c2, 4)}")
    print(f"Cell(12) по 5:\n{Cell.make_order(Cell(12), 5)}")
    print(f"Cell(15) по 5:\n{Cell.make_order(Cell(15), 5)}")
    print("Stop")