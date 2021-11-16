# Проверить механизм наследования в Python. Для этого создать два класса. Первый —
# родительский (ItemDiscount), должен содержать статическую информацию о товаре: название
# и цену. Второй — дочерний (ItemDiscountReport), должен содержать функцию
# (get_parent_data), отвечающую за отображение информации о товаре в одной строке.
# Проверить работу программы, создав экземпляр (объект) родительского класса.
from typing import Union


class ItemDiscount:
    def __init__(self, name: str, price: Union[int, float]):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self) -> str:
        return f'{self.name}: {self.price} руб.'


if __name__ == '__main__':
    item_discount = ItemDiscount('стул', 2000)

    item_discount_report = ItemDiscountReport('стул', 2000)
    print(item_discount_report.get_parent_data())
