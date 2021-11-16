# Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс
# ItemDiscountReport на два класса. Инициализировать классы необязательно. Внутри каждого
# поместить функцию get_info, которая в первом классе будет отвечать за вывод названия
# товара, а вторая — его цены. Далее реализовать выполнение каждой из функции тремя
# способами.
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
    def price(self, value: Union[int, float]):
        if isinstance(value, int) or isinstance(value, float):
            self.__price = value
        else:
            print('Введите число.')


class ItemDiscountReport1(ItemDiscount):
    def __init__(self, name: str, price: Union[int, float], discount: int):
        super().__init__(name, price)
        self.discount = discount

    def get_parent_data(self) -> str:
        return f'{self.name}: {self.price} руб.'

    def __str__(self):
        return f'Цена товара со скидкой: {self.price - self.price * self.discount / 100} руб.'

    def get_info(self):
        print(self.name)


class ItemDiscountReport2(ItemDiscount):
    def __init__(self, name: str, price: Union[int, float], discount: int):
        super().__init__(name, price)
        self.discount = discount

    def get_parent_data(self) -> str:
        return f'{self.name}: {self.price} руб.'

    def __str__(self):
        return f'Цена товара со скидкой: {self.price - self.price * self.discount / 100} руб.'

    def get_info(self):
        print(self.price)


if __name__ == '__main__':
    item_discount_report1 = ItemDiscountReport1('Стол', 3500, 5)
    item_discount_report2 = ItemDiscountReport2('Стул', 2000, 10)

    for item in (item_discount_report1, item_discount_report2):
        item.get_info()
