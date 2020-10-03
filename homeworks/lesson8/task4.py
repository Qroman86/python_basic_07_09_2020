#task4, task5, task6
"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
 изученных на уроках по ООП.
"""
from typing import List


class OfficeEquipment:

    __inventory_number = -1


    def __init__(self, vendor: str, model: str):
        self.__vendor = vendor
        self.__model = model

    @property
    def inventory_number(self):
        return self.__inventory_number


    @property
    def vendor(self):
        return self.__vendor

    @property
    def model(self):
        return self.__model

    @inventory_number.setter
    def inventory_number(self, inventory_number: int):
        if inventory_number < 1:
            raise ValueError("Инвентарный номер должен быть целым положительным числом")
        self.__inventory_number = inventory_number

    @property
    def max_resolution_dpi(self):
        return self.__max_resolution_dpi

    @max_resolution_dpi.setter
    def max_resolution_dpi(self, max_resolution_dpi: str):
        self.__max_resolution_dpi = max_resolution_dpi

    @property
    def max_format(self):
        return self.__max_format

    @max_format.setter
    def max_format(self, max_format: str):
        self.__max_format = max_format


class Printer(OfficeEquipment):
    def __init__(self, vendor: str, model: str):
        super(Printer, self).__init__(vendor, model)



    @property
    def is_color(self):
        return self.__is_color

    @is_color.setter
    def is_color(self, is_color: bool):
        self.__is_color = is_color

    @property
    def print_speed(self):
        return self.__print_speed

    @print_speed.setter
    def print_speed(self, print_speed: int):
        self.__print_speed = print_speed



    @property
    def print_tech(self):
        return self.__print_tech

    @print_tech.setter
    def print_tech(self, print_tech: str):
        self.__print_tech = print_tech

    @property
    def color_type(self):
        if self.is_color:
            return "цветная"
        return "черно-белая"


    def __str__(self):
        return f"\nИнвентарный номер: {self.inventory_number}\n" \
               f"Тип оргтехники: Принтер\n" \
               f"Производитель: {self.vendor}\n" \
               f"Модель: {self.model}\n" \
               f"Маскимальный формат: {self.max_format}\n" \
               f"Цветность печати: {self.color_type}\n" \
               f"Скорость печати (кол-во страниц в минуту): {self.print_speed}\n" \
               f"Максимальное разрешение dpi: {self.max_resolution_dpi}\n" \
               f"Технология печати: {self.print_tech}\n"


class Scanner(OfficeEquipment):
    def __init__(self, vendor: str, model: str):
        super(Scanner, self).__init__(vendor, model)


    @property
    def is_send_email(self):
        return self.__is_send_email

    @is_send_email.setter
    def is_send_email(self, is_send_email: bool):
        self.__is_send_email = is_send_email

    @property
    def grey_shades(self):
        return self.__grey_shades

    @grey_shades.setter
    def grey_shades(self, grey_shades: int):
        self.__grey_shades = grey_shades

    def __str__(self):
        return f"\nИнвентарный номер: {self.inventory_number}\n" \
               f"Тип оргтехники: Сканер\n" \
               f"Производитель: {self.vendor}\n" \
               f"Модель: {self.model}\n" \
               f"Маскимальный формат: {self.max_format}\n" \
               f"Максимальное разрешение dpi: {self.max_resolution_dpi}\n" \
               f"Отправка по email: {self.is_send_email}\n" \
               f"Оттенки серого: {self.grey_shades}\n"


class Copier(OfficeEquipment):
    def __init__(self, vendor: str, model: str):
        super(Copier, self).__init__(vendor, model)


    @property
    def copy_speed(self):
        return self.__copy_speed

    @copy_speed.setter
    def copy_speed(self, copy_speed: int):
        self.__copy_speed = copy_speed



    def __str__(self):
        return f"\nИнвентарный номер: {self.inventory_number}\n" \
               f"Тип оргтехники: Ксерокс\n" \
               f"Производитель: {self.vendor}\n" \
               f"Модель: {self.model}\n" \
               f"Маскимальный формат: {self.max_format}\n" \
               f"Скорость копирования (кол-во страниц в минуту): {self.copy_speed}\n" \
               f"Максимальное разрешение dpi: {self.max_resolution_dpi}\n" \

#Класс, описывающий склад
class Warehouse:
    def __init__(self):
        self.__items = []
        self.__inventory_number_counter = 0
        self.__dict_item_location_by_number = {}


    def check_is_number_in_warehouse(self, number: int):
        return number in self.__dict_item_location_by_number.keys()

    @property
    def inventory_number_counter(self):
        return self.__inventory_number_counter

    def receive_office_equipment_by_number(self, inventory_number: int):
        """
            Принять единицу оргтехники по инвентарному номеру
        """
        if not self.check_is_number_in_warehouse(inventory_number):
            raise ValueError(f"Номер {inventory_number} не включен в складской список")
        self.__dict_item_location_by_number.update({inventory_number: "Склад"})

    def receive_office_equipment(self, inventory_item: OfficeEquipment):
        """
            Принять оргтехнику на склад
        """
        if inventory_item.inventory_number < 1:
            self.add_new_inventory_item(inventory_item)
        #если оргтехника не имеет инвентарный номер необходимо добавить запись
        self.receive_office_equipment_by_number(inventory_item.inventory_number)

    def transfer_to_company_division_by_number(self, inventory_number: int, division_name: str):
        if not division_name:
            raise ValueError("Не указано название подразделения")
        if inventory_number not in self.__dict_item_location_by_number.keys():
            raise ValueError(
                f"Указанный инвентарный номер {inventory_number} отсутствует в списке единиц учета оргтехники")
        self.__dict_item_location_by_number.update({inventory_number: division_name})

    def transfer_to_company_division(self, inventory_item: OfficeEquipment, division_name: str):
        """
            Передать оргтехнику подразделению
        """
        self.transfer_to_company_division_by_number(inventory_item.inventory_number, division_name)

    def add_new_inventory_item(self, inventory_item: OfficeEquipment):
        """
            Добавить информацию о новой единице оргтехнике хранения
        """
        self.__inventory_number_counter += 1
        inventory_item.inventory_number = self.__inventory_number_counter
        inventory_item.warehouse = self
        self.__items.append(inventory_item)
        self.__dict_item_location_by_number.update({inventory_item.inventory_number: "Склад"})

    def prepare_print_data(self, inventory_item: OfficeEquipment) -> str:
        return f"{'-'*18}\n {str(inventory_item)}Текущее место дислокации: {self.__dict_item_location_by_number.get(inventory_item.inventory_number)}"

    def __str__(self):
        return f"\n{'*'*16}\nЕдиницы техники, приписанные к складу" + "\n".join(self.prepare_print_data(item) for item in self.__items)


class UserInterface:
    @staticmethod
    def transfer_to_division_by_vendor_model(warehouse: Warehouse, vendor: str, model: str, number: int):
        """
            Передать в указанное подразделение указанное количество оргтехники с указанием производителя и модели
        """
        pass

    @staticmethod
    def recieve_to_warehouse_by_inventory_id(warehouse: Warehouse, inventory_id: int):
        """
            Вернуть на склад по указанному номеру id
        """
        pass

    @staticmethod
    def print_commands_info():
        """
        Вывести список команд
        """
        commands_info = "\nСписок команд:\n" \
                        "help - вывести список команд\n" \
                        "exit - выйти из программы\n" \
                        "print - вывести информацию учета по складу\n" \
                        "recieve - принять на склад технику\n" \
                        "transfer - передать в подразделение\n"
        print(commands_info)

    @staticmethod
    def convert_str_to_number_list(inv_list_str: str):
        inv_list_split = inv_list_str.split(' ')
        if len(inv_list_split) == 0:
            raise ValueError("Введенный список инвентарных номеров пуст")
        number_list = []
        for inv_item in inv_list_split:
            try:
                number_list.append(int(inv_item))
            except ValueError:
                raise ValueError(f"Введенный список инвентарных номеров содержит {inv_item} нечисло или число не явлющимся целым положительным числом")
        return number_list

    @staticmethod
    def check_number_for_warehouse(warehouse: Warehouse, number_list: List):
        for number in number_list:
            if not warehouse.check_is_number_in_warehouse(number):
                raise ValueError(f"В складском учете нет оргтехники с указанным номером {number}")

    @staticmethod
    def recieve_invetory_items(warehouse: Warehouse, number_list: List):
        for number in number_list:
            warehouse.receive_office_equipment_by_number(number)

    @staticmethod
    def transfer_invetory_items(warehouse: Warehouse, number_list: List, division_name: str):
        for number in number_list:
            warehouse.transfer_to_company_division_by_number(number, division_name)

    @staticmethod
    def recieve(warehouse: Warehouse):
        while True:
            inv_list_str = input(f"Для возврата на склад введите список инвентарных номеров единиц оргтехники, разделенных пробелом:\n")
            try:
                number_list = UserInterface.convert_str_to_number_list(inv_list_str)
                UserInterface.check_number_for_warehouse(warehouse, number_list)
                UserInterface.recieve_invetory_items(warehouse, number_list)
                break
            except ValueError as e:
                print(e)
                continue

    @staticmethod
    def transfer(warehouse: Warehouse):
        while True:
            org_division_name = input(f"Введите наименование подразделения, куда следует передать оргтехнику:\n")
            if not org_division_name:
                print("Название подразделения не должно быть пустым")
                continue

            inv_list_str = input(f"Для передачи со склада введите список инвентарных номеров единиц оргтехники, разделенных пробелом:\n")
            try:
                number_list = UserInterface.convert_str_to_number_list(inv_list_str)
                UserInterface.check_number_for_warehouse(warehouse, number_list)
                UserInterface.transfer_invetory_items(warehouse, number_list, org_division_name)
                break
            except ValueError as e:
                print(e)
                continue

    @staticmethod
    def print_warehouse_data(warehouse: Warehouse):
        print(warehouse)

    @staticmethod
    def main_process(warehouse: Warehouse):
        """
        Основной процесс работы с пользовательской строкой
        """
        while True:
            command = input("Система складского учета. Введите команду (exit - выход, help - список команд):\n")
            if command == 'exit':
                break
            elif command == 'help':
                UserInterface.print_commands_info()
            elif command == 'print':
                UserInterface.print_warehouse_data(warehouse)
            elif command == 'recieve':
                UserInterface.recieve(warehouse)
            elif command == 'transfer':
                UserInterface.transfer(warehouse)
            else:
                print("Введенная команда не поддерживается")
                UserInterface.print_commands_info()

if __name__  == '__main__':
    #task4
    print("TASK #4")
    warehouse = Warehouse()

    printer1 = Printer("Canon", "12324344")
    printer1.max_format = "A4"
    printer1.print_speed = 20
    printer1.print_tech = "laser"
    printer1.is_color = False
    printer1.max_resolution_dpi = "1200x1200 dpi"

    warehouse.add_new_inventory_item(printer1)
    print(printer1)
    print("Текущее максимальное значение инвентарного номера", warehouse.inventory_number_counter)

    scanner1 = Scanner("JWS", "32374834")
    scanner1.max_format = "A3"
    scanner1.is_send_email = True
    scanner1.grey_shades = 256
    scanner1.max_resolution_dpi = "1200x1200 dpi"

    warehouse.add_new_inventory_item(scanner1)
    print(scanner1)
    print("Текущее максимальное значение инвентарного номера", warehouse.inventory_number_counter)

    coppier1 = Copier("TYO", "3434343")
    coppier1.max_format = "A4"
    coppier1.copy_speed = 25
    coppier1.max_resolution_dpi = "600x600 dpi"

    warehouse.add_new_inventory_item(coppier1)
    print(coppier1)
    print("Текущее максимальное значение инвентарного номера", warehouse.inventory_number_counter)

    print(warehouse)

    #task5
    print("\n\nTASK #5")
    warehouse.transfer_to_company_division(printer1, "Бухгалтерия")
    coppier2 = Copier("APPOLLO", "23394")
    coppier2.max_format = "A3"
    coppier2.copy_speed = 30
    coppier2.max_resolution_dpi = "1200x1200 dpi"
    warehouse.receive_office_equipment(coppier2)
    print("\n\nУчет после передачи принтера в Бухгалтерию и приемки нового ксерокса:")
    print(warehouse)
    warehouse.receive_office_equipment(printer1)
    print("\n\nУчет после возвращения принтера из Бухгалтерию на склад:")
    print(warehouse)

    # task6
    print("\n\nTASK #6")
    #Добавление информации о нескольких сканерах одной модели
    scanner2 = Scanner("JWS", "32374834")
    scanner2.max_format = "A3"
    scanner2.is_send_email = True
    scanner2.grey_shades = 256
    scanner2.max_resolution_dpi = "1200x1200 dpi"
    warehouse.receive_office_equipment(scanner2)

    scanner3 = Scanner("JWS", "32374834")
    scanner3.max_format = "A3"
    scanner3.is_send_email = True
    scanner3.grey_shades = 256
    scanner3.max_resolution_dpi = "1200x1200 dpi"
    warehouse.receive_office_equipment(scanner3)

    scanner4 = Scanner("JWS", "32374834")
    scanner4.max_format = "A3"
    scanner4.is_send_email = True
    scanner4.grey_shades = 256
    scanner4.max_resolution_dpi = "1200x1200 dpi"
    warehouse.receive_office_equipment(scanner4)

    UserInterface.main_process(warehouse)