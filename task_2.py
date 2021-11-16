# Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться,
# что при сохранении текущей логики работы программы будет сгенерирована ошибка
# выполнения. Усовершенствовать родительский класс таким образом, чтобы получить доступ к
# защищенным переменным. Результат выполнения заданий 1 и 2 должен быть идентичным.
from typing import Union


class ItemDiscount:
    def __init__(self, name: str, price: Union[int, float]):
        self.__name = name
        self.__price = price

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self) -> str:
        return f'{self.get_name}: {self.get_price} руб.'


if __name__ == '__main__':
    item_discount = ItemDiscount('стул', 2000)

    item_discount_report = ItemDiscountReport('стул', 2000)
    print(item_discount_report.get_parent_data())
