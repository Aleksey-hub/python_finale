# Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и
# родительский, и дочерний классы получили новое значение цены. Следует проверить это,
# вызвав соответствующий метод родительского класса и функцию дочернего (функция,
# отвечающая за отображение информации о товаре в одной строке).
from typing import Union


class ItemDiscount:
    def __init__(self, name: str, price: Union[int, float]):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__price = value
        else:
            print('Введите число.')


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self) -> str:
        return f'{self.name}: {self.price} руб.'


if __name__ == '__main__':
    item_discount_report = ItemDiscountReport('стул', 2000)
    print(item_discount_report.get_parent_data())

    item_discount_report.price = 999
    print(item_discount_report.get_parent_data())
