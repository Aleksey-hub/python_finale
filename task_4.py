# Написать программу, в которой реализовать две функции. В первой должен создаваться
# простой текстовый файл. Если файл с таким именем уже существует, выводим
# соответствующее сообщение. Необходимо открыть файл и подготовить два списка: с
# текстовой и числовой информацией. Для создания списков использовать генераторы.
# Применить к спискам функцию zip(). Результат выполнения этой функции должен должен быть
# обработан и записан в файл таким образом, чтобы каждая строка файла содержала текстовое
# и числовое значение. Вызвать вторую функцию. В нее должна передаваться ссылка на
# созданный файл. Во второй функции необходимо реализовать открытие файла и простой
# построчный вывод содержимого. Вся программа должна запускаться по вызову первой
# функции.
import string
from random import randint, choice
from typing import TextIO

NUMBER_ROWS = 10


def read_file(file: TextIO) -> None:
    file.seek(0, 0)
    for string in file:
        print(string, end='')


def random_word_generator(min_count_letters: int = 3, max_count_letters: int = 10) -> str:
    random_word_list = [choice(string.ascii_letters) for _ in range(min_count_letters, max_count_letters + 1)]
    return ''.join(random_word_list)


def create_file(file_name: str, number_rows: int = NUMBER_ROWS) -> None:
    list_number = [randint(1, 1000) for _ in range(1, number_rows + 1)]
    list_text = [random_word_generator() for _ in range(1, number_rows + 1)]

    union_list = list(zip(list_number, list_text))
    try:
        with open(file_name, 'x+', encoding='utf-8') as f:
            for string in union_list:
                f.write(f'{string[0]} {string[1]}\n')
            read_file(f)
    except FileExistsError:
        print(f'Файл с именем {file_name} уже существует.')


if __name__ == '__main__':
    file = create_file('text.txt')
