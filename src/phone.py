from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """Геттер для кол-ва симкарт"""
        return self.__number_of_sim   #  чтобы через конструктор можно было создать только положительное кол-во симкарт
    @number_of_sim.setter
    def number_of_sim(self, new_number):
        """сеттер для кол-ва симкарт"""
        if new_number > 0 and isinstance(new_number, int):
            self.__number_of_sim = new_number
        raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")

