"""
3. Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0.0, "bonus": 0.0}

    def __init__(self, name_value: str, surname_value: str, position: str, wage: float, bonus: float):
        self.name = name_value
        self.surname = surname_value
        self.position = position
        self._income.update({"wage": wage})
        self._income.update({"bonus": bonus})


class Position(Worker):
    def get_full_name(self) -> str:
        """
         Вывести полное имя
        :return: полное имя
        """
        return  f"{self.name} {self.surname}"


    def get_total_income(self) -> float:
        """
        Вырнуть суммарное значение дохода
        :return: суммарное значение дохода
        """
        try:
            return float(self._income.get("wage")) + float(self._income.get("bonus"))
        except ValueError:
            return 0.0


def print_full_data(position: Position):
    """
    Вывести информацию по экземпляру класса Position
    :param position: экземпляр класса Position c данными по должности
    :return:
    """
    print(f"\nИмя: {position.name}")
    print(f"Фамилия: {position.surname}")
    print(f"Должность: {position.position}")
    print(f"Полное имя: {position.get_full_name()}")
    print(f"Совокупный доход: {position.get_total_income()}")


if __name__ == '__main__':
    ceo = Position("Иван", "Петров", "CEO", 100000, 25000)
    assert ceo.get_full_name() == "Иван Петров", "Тест на формирование полного имени провален"
    assert ceo.get_total_income() == 125000, "Тест на расчет суммарного дохода провален"
    print_full_data(ceo)

    tester = Position("Джамшут", "Махараджи", "Tester", 50000, 10000)
    print_full_data(tester)

    developer = Position("Фарид", "Акопян", "Developer", 70000, 18000)
    print_full_data(developer)