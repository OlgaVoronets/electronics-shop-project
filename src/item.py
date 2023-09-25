import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)  # при создании экземпляра класса добавляет его в общий список

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """геттер для name"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """сеттер для name"""
        if len(new_name) > 10:
            self.__name = new_name[:10]
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls, file_name):
        """Инициализирует экземпляры класса `Item` данными из файла .csv"""
        dir_ = os.path.dirname(__file__)
        file_path = os.path.join(dir_, file_name)
        with open(file_path, encoding='cp1251') as file:
            content = csv.DictReader(file)
            for dict_ in content:
                name = dict_['name']
                price = float(dict_['price'])
                quantity = int(dict_['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(str_):
        """Возвращает число из числа-строки"""
        return int(float(str_))
