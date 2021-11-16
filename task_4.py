# Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в
# качестве аргумента в дочерний класс. Выполнить перегрузку методов конструктора дочернего
# класса (метод __init__, в который должна передаваться переменная — скидка), и перегрузку
# метода __str__ дочернего класса. В этом методе должна пересчитываться цена и
# возвращаться результат — цена товара со скидкой. Чтобы все работало корректно, не
# забудьте инициализировать дочерний и родительский классы (вторая и третья строка после
# объявления дочернего класса).
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


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name: str, price: Union[int, float], discount: int):
        super().__init__(name, price)
        self.discount = discount

    def get_parent_data(self) -> str:
        return f'{self.name}: {self.price} руб.'

    def __str__(self):
        return f'Цена товара со скидкой: {self.price - self.price * self.discount / 100} руб.'


if __name__ == '__main__':
    item_discount = ItemDiscount('стул', 2000)

    item_discount_report = ItemDiscountReport('стул', 2000, 10)
    print(item_discount_report.get_parent_data())
    print(item_discount_report)
