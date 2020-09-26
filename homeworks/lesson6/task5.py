"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = ""

    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print(f"Отрисовка ручкой {self.title}")


class Pencil(Stationery):

    def draw(self):
        print(f"Отрисовка карандашом {self.title}")


class Handle(Stationery):

    def draw(self):
        print(f"Отрисовка маркером {self.title}")


if __name__ == '__main__':
    stat = Stationery("предмет")
    stat.draw()

    pen = Pen("гелевая ручка")
    pen.draw()

    pencil = Pencil("грифельный карандаш")
    pencil.draw()

    handle = Handle("несмываемый маркер")
    handle.draw()