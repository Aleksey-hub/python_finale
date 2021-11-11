import os


# Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath: str) -> None:
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.
    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """
    # заполните далее
    listdir_ = os.listdir(sPath)
    print(sPath, listdir_)

    for file_or_dir in listdir_:
        path_file_or_dir = os.path.join(sPath, file_or_dir)

        if os.path.isdir(path_file_or_dir):
            print_directory_contents(path_file_or_dir)


if __name__ == '__main__':
    print_directory_contents('C:\Python\Python3.9')
