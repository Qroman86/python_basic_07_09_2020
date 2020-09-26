"""
1. Создать класс TrafficLight (светофор) и определить у него
один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time


class TrafficLight:
    RED = "Red"
    YELLOW = "Yellow"
    GREEN = "Green"
    OFF = "Off"
    __color = OFF

    def change_color(self, new_color: str, time_value: int):
        __color = new_color
        print(f"Traffic light color is {__color}")
        time.sleep(time_value)

    def running(self):
        self.change_color(self.RED, 7)
        self.change_color(self.YELLOW, 2)
        self.change_color(self.GREEN, 5)
        self.change_color(self.OFF, 5)


if __name__ == '__main__':
    traffic_ligth = TrafficLight()
    traffic_ligth.running()