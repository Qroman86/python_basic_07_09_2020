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


    @property
    def inventory_number_counter(self):
        return self.__inventory_number_counter


    def receive_office_equipment(self, inventory_item: OfficeEquipment):
        """
            Принять оргтехнику на склад
        """
        #если оргтехника не имеет инвентарный номер необходимо добавить запись
        if inventory_item.inventory_number < 1:
            self.add_new_inventory_item(inventory_item)
        else:
            # Делаем запись, что оргтехника на складе
            self.__dict_item_location_by_number.update({inventory_item.inventory_number: "Склад"})


    def transfer_to_company_division(self, inventory_item: OfficeEquipment, division_name: str):
        """
            Передать оргтехнику подразделению
        """
        if not division_name:
            raise ValueError("Не указано название подразделения")
        if inventory_item.inventory_number not in self.__dict_item_location_by_number.keys():
            raise ValueError(f"Указанный инвентарный номер {inventory_item.inventory_number} отсутствует в списке единиц учета оргтехники")
        self.__dict_item_location_by_number.update({inventory_item.inventory_number: division_name})

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
    def

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