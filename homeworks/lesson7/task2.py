from abc import ABC, abstractmethod

class Clothing(ABC):

    def __init__(self, *args):
        self._name = "Одежда"

    @property
    @abstractmethod
    def fabric_consumption(self) -> float:
        pass

    @property
    def name(self):
        return self._name


class Coat(Clothing):

    def __init__(self, size: float, *args):
        super(Coat, self).__init__()
        self._name = "Пальто"
        self.__size = size

    @property
    def fabric_consumption(self) -> float:
        return self.size / 6.5 + 0.5

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 0:
            size = 0
        self.__size = size


class Suit(Clothing):

    def __init__(self, growth: float, *args):
        super(Suit, self).__init__()
        self._name = "Костюм"
        self.__growth = growth

    @property
    def fabric_consumption(self) -> float:
        return 2 * self.growth + 0.3

    @property
    def growth(self):
        return self.__growth

    @growth.setter
    def growth(self, growth):
        if growth < 0:
            growth = 0
        self.__growth = growth

if __name__ == '__main__':
    coat = Coat(3)
    print(coat.name)
    print(coat.fabric_consumption)

    coat.size = 6.5
    assert coat.fabric_consumption == 1.5, "Неверный расчет для пальто"

    suit = Suit(4)
    print(suit.name)
    print(suit.fabric_consumption)

    suit.growth = 1
    assert suit.fabric_consumption == 2.3, "Неверный расчет для костюма"