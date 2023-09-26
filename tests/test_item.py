"""Здесь надо написать тесты с использованием pytest для модуля item."""


from src.item import Item

# item1 = Item("Смартфон", 10000, 20)
# item2 = Item("Ноутбук", 20000, 5)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_pay_rate():
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000


def test_name_length():
    item = Item('Телефон', 10000, 5)
    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    assert item.name == "СуперСмарт"


def test_instantiate_from_csv():
    Item.instantiate_from_csv('items.csv')  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr_str():
    item1 = Item("Смартфон", 10000, 20)

    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
    assert str(item1) == 'Смартфон'









