# Написать программу, которая будет содержать функцию для получения имени файла из
# полного пути до него. При вызове функции в качестве аргумента должно передаваться имя
# файла с расширением. В функции необходимо реализовать поиск полного пути по имени
# файла, а затем «выделение» из этого пути имени файла (без расширения).
import os


def get_name_file(full_name_file: str) -> str:
    abs_path = os.path.abspath(full_name_file)

    start_index = abs_path.rfind(os.sep) + 1
    end_index = abs_path.rfind('.')
    file_name = abs_path[start_index:end_index]
    return file_name


if __name__ == '__main__':
    print(get_name_file('task_1.py'))
