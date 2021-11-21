# Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке
# часть строковых значений заменить на значения типа example345 (строка+число). Далее —
# усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных).
# Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
# вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных
# подстрок на новое значение и вывод всех подстрок, состоящих из букв и цифр и имеющих
# пробелы только в начале и конце — например, example345.
import re
import string
from random import randint, choice
from typing import TextIO

NUMBER_ROWS = 10


def read_file(file: TextIO, substring: str, new_string: str) -> None:
    file.seek(0, 0)

    file_new = []
    for string in file:
        if string.find(substring) != -1 or re.search(r'\d+ \w+\d+', string):
            file_new.append(new_string)
        else:
            file_new.append(string)

    for string in file_new:
        print(string, end='')


def random_word_generator(min_count_letters: int = 3, max_count_letters: int = 10) -> str:
    random_word_list = [choice(string.ascii_letters) for _ in range(min_count_letters, max_count_letters + 1)]
    word_int_suffix = str(randint(100, 1000)) if randint(0, 1) else ''
    return ''.join(random_word_list) + word_int_suffix


def create_file(file_name: str, number_rows: int = NUMBER_ROWS) -> None:
    list_number = [randint(1, 1000) for _ in range(1, number_rows + 1)]
    list_text = [random_word_generator() for _ in range(1, number_rows + 1)]

    union_list = list(zip(list_number, list_text))
    try:
        with open(file_name, 'x+', encoding='utf-8') as f:
            for string in union_list:
                f.write(f'{string[0]} {string[1]}\n')
            read_file(f, 'z', 'qwe123\n')
    except FileExistsError:
        print(f'Файл с именем {file_name} уже существует.')


if __name__ == '__main__':
    file = create_file('text_2.txt')
