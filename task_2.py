# Написать программу, которая запрашивает у пользователя ввод числа. На введенное число
# она отвечает сообщением, целое оно или дробное. Если дробное — необходимо далее
# выполнить сравнение чисел до и после запятой. Если они совпадают, программа должна
# возвращать значение True, иначе False.
from typing import Union, Optional


def comparing_numbers(number: Union[int, float]) -> Optional[bool]:
    if isinstance(number, int):
        print(f'Число {number} целое')
        return None
    elif isinstance(number, float):
        print(f'Число {number} дробное')

        number_before_point = number // 1

        number_after_point = number % 1
        point_index_from_end = len(str(number)) - str(number).find('.') - 1
        number_after_point = number_after_point * (10 ** point_index_from_end)
        number_after_point = round(number_after_point)

        if number_before_point == number_after_point:
            return True
        else:
            return False
    else:
        print('Введите число')
        return None


if __name__ == '__main__':
    print(comparing_numbers('task_1.py'))
    print(comparing_numbers(5))
    print(comparing_numbers(55.55))
