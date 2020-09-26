"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

class Road:
    __length = 0.0
    __width = 0.0

    def __init__(self, length: float, width: float):
        self.__length = length
        self.__width = width


    def calc_total_weight(self, weight_per_one_sq_meter: float, road_bed_thickness: float) -> float:
        """
        Расчет суммарной массы полотна дороги в кг
        :param weight_per_one_sq_meter: вес полотна толщиной в 1 см и площадью 1 кв. м в кг
        :param road_bed_thickness: толщина полотна в см
        :return: суммарный вес полотна дороги в т
        """
        total_weght = self.__length * self.__width * weight_per_one_sq_meter * road_bed_thickness
        total_weght /= 1000
        return total_weght


def ask_float(prompt_str: str) -> float:
    """
    Запросить у пользователя числовое значение
    :param prompt_str: строка с запросом к пользователю
    :return: введенное числовое значение
    """
    while True:
        value = 0
        try:
            value = float(input(prompt_str))
        except ValueError as e:
            print("Введенное значение не является числом")
        if value <= 0:
            print("Введеное значение не является положительным числом")
            continue
        return value


def check_calc():
    """
    Метод, выполняющий тестирование
    :return:
    """
    test_road = Road(5000, 20)
    assert test_road.calc_total_weight(25, 5) == 12500, "Неверно работает метод расчета требуемой массы асфальта"


if __name__ == '__main__':
    check_calc()

    road_length = ask_float("Введите длину дороги в метрах:\n")
    road_width = ask_float("Введите ширину дороги в метрах:\n")
    road_M1 = Road(road_length, road_width)

    weight_per_one_sq_meter = ask_float("Введите массу асфальта для покрытия одного кв. метра асфальта толщиной в 1 см в кг:\n")
    road_bed_thickness = ask_float("Введите толщину полотна дороги в см:\n")
    total_weigth = road_M1.calc_total_weight(weight_per_one_sq_meter, road_bed_thickness)
    print(f"\nМасса асфальта, требуемая для покрытия указанной дороги равна {total_weigth} т")