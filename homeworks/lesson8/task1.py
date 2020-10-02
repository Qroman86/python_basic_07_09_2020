"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    __day = 0
    __month = 0
    __year = 0

    def __init__(self, date_str: str):
        try:

            day_value, month_value, year_value = Date.convert_str_to_numbers(date_str)
            Date.validate_date_numbers(day_value, month_value, year_value)
            self.__day = day_value
            self.__month = month_value
            self.__year = year_value
        except ValueError as e:
            print(f"Перехвачена ошибка для вводимой строки '{date_str}':\n {e}")

    @classmethod
    def convert_str_to_numbers(cls, date_str: str):
        if not date_str:
            raise ValueError("Передана пустая строка")
        date_str_split = date_str.split("-")
        if len(date_str_split) != 3:
            raise ValueError("Переданная строка не соответствует формату DD-MM-YYYY")

        try:
            day_number = int(date_str_split[0])
            month_number = int(date_str_split[1])
            year_number = int(date_str_split[2])
            return day_number, month_number, year_number
        except ValueError:
            raise ValueError("Переданная строка не соответствует формату DD-MM-YYYY")


    @staticmethod
    def validate_date_numbers(day_value: int, month_value: int, year_value: int):
        if year_value < 1:
            raise ValueError("Значение года должно быть чилом большим нуля")
        if month_value < 1 or month_value > 12:
            raise ValueError("Значение номера месяца должно быть чилом в диапазоне от 1 до 12")

        month_days_count =  {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        is_leap_year = year_value % 4 == 0 and (not year_value % 100 == 0 or year_value % 400 == 0)
        if is_leap_year:
            month_days_count.update({2: 29})

        if day_value < 1 or day_value > month_days_count[month_value]:
            raise ValueError(f"Значение числа дня месяца №{month_value} года {year_value} должно быть чиcлом в диапазоне от 1 до {month_days_count[month_value]}")


    @property
    def day(self):
        return self.__day


    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    def __str__(self):
        return f"Date day {self.day} month {self.month} year {self.year}"

if __name__  == '__main__':
    date1 = Date("01-02-2019")
    print(date1)
    date2 = Date("07-09-1914")
    print(date2)
    date3 = Date("31-02-1914")
    print(date3)
    date3 = Date("05-24-1988")
    print(date3)
    date3 = Date("29-02-2020")
    print(date3)
