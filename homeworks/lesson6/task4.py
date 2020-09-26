"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    _speed = 0.0
    _color = "not defined"
    _name = ""
    _is_police = False

    def __init__(self, name: str, color: str):
        self._name = name
        self._color = color

    def go(self):
        self._speed = 5.0
        print(f"машина {self._name} поехала")

    def stop(self):
        self._speed = 0.0
        print(f"машина {self._name} остановилась")

    def turn(self, direction: str):
        print(f"машина {self._name} повернула в направлении {direction}")

    def set_speed(self, speed_value: float):
        if speed_value < 0:
            print("Заданное значение скорости не может отрицательным")
        else:
            self._speed = speed_value

    def show_speed(self):
        print(f"Текущее значение скорости для машины {self._name} равно {self._speed}")

    def get_speed(self):
        return self._speed

    def get_color(self):
        return self._color

    def get_name(self):
        return self._name

    def get_is_police(self):
        return self._is_police


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self._speed > 60:
            print(f"Превышение скорости для машины {self._name} выше 60 км/ч")

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self._speed > 40:
            print(f"Превышение скорости для машины {self._name} выше 40 км/ч")

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)
        self._is_police = True


def create_and_run_car(car: Car):
    """
    Унифиуированный тестовыц сценарий для любой машины
    :param car: объект с данными машины
    :return:
    """
    print("\nИнформация по машине")
    print(f"Название машины: {car.get_name()}")
    print(f"Цвет машины: {car.get_color()}")
    print(f"Скорость машины: {car.get_speed()}")
    print(f"Является ли машина полицеской: {car.get_is_police()}")

    print("\nСтарт тестового сценария")
    car.go()
    car.show_speed()
    car.set_speed(20)
    car.show_speed()
    car.set_speed(30)
    car.show_speed()
    car.set_speed(50)
    car.show_speed()
    car.set_speed(60)
    car.show_speed()
    car.set_speed(70)
    car.show_speed()
    car.turn("налево")
    car.show_speed()
    car.turn("направо")
    car.show_speed()
    car.stop()
    car.show_speed()

if __name__ == '__main__':
    town_car = TownCar("Грузовик", "белый")
    create_and_run_car(town_car)

    sport_car = SportCar("Ламборджини", "розовый")
    create_and_run_car(sport_car)

    police_car = PoliceCar("патруль", "сине-белый")
    create_and_run_car(police_car)

    work_car = WorkCar("Трактор", "черный")
    create_and_run_car(work_car)