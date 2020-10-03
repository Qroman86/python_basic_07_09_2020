"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class Complex:
    """
           Представление комплексного числа: x + y * i
    """
    def __init__(self, x: float, y: float):

        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    def __add__(self, other):
        if not isinstance(other, Complex):
            raise TypeError("Второй операнд не является экземпляром класса Complex")
        return Complex(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if not isinstance(other, Complex):
            raise TypeError("Второй операнд не является экземпляром класса Complex")
        x_value = self.x * other.x - self.y * other.y
        y_value = self.x * other.y + other.x * self.y
        return Complex(x_value, y_value)

    def __str__(self):
        return f"{self.x} + {self.y} * i"

if __name__  == '__main__':
    z1 = Complex(1, 4)
    z2 = Complex(3, -2)
    z3 = z1 + z2
    assert z3.x == 4 and z3.y == 2 , "Неверно выполняется операция сложения для комплексных чисел"
    print(f"z1 + z2 = {z3}")
    z4 = z1 * z2
    assert z4.x == 11 and z4.y == 10, "Неверно выполняется операция умножения для комплексных чисел"
    print(f"z1 * z2 = {z4}")