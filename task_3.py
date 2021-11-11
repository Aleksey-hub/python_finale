# Разработать генератор случайных чисел. В функцию передавать начальное и конечное число
# генерации (нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи
# словаря должны создаваться по шаблону: “elem_<номер_элемента>”. Вывести содержимое
# созданных списка и словаря.
import time
from typing import Union


class Rand:
    def __init__(self):
        self.number_init = 0

    def random_generator(self, start_number: Union[int, float], final_number: Union[int, float]) -> float:
        if not self.number_init:
            self.number_init = (start_number + final_number) / 2
        rand_number = start_number + time.time() * self.number_init % (final_number - start_number)
        self.number_init = rand_number

        return rand_number


if __name__ == '__main__':
    START_NUMBER = 10
    FINAL_NUMBER = 100
    COUNT_RANDOM_NUMBER = 30

    random_list = []
    random_dict = {}
    rand = Rand()
    for i in range(1, COUNT_RANDOM_NUMBER + 1):
        random_number = rand.random_generator(START_NUMBER, FINAL_NUMBER)

        random_list.append(random_number)
        key_dict = f'elem_{i}'
        random_dict[key_dict] = random_number

    print(random_list)
    print(random_dict)
