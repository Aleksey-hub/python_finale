# Написать функцию, реализующую вывод таблицы умножения размерностью AｘB. Первый и
# второй множитель должны задаваться в виде аргументов функции. Значения каждой строки
# таблицы должны быть представлены списком, который формируется в цикле. После этого
# осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку.
# Полученная строка выводится в главной функции. Элементы строки (элементы таблицы
# умножения) должны разделяться табуляцией.

def multiplication_table(A: int, B: int) -> None:
    for a in range(0, A + 1):
        # формирование 1-й строки таблицы
        if a == 0:
            string_table = ['']
            for b in range(1, B + 1):
                string_table.append(b)
        # формирование остальных строк таблицы
        else:
            string_table = [a]
            for b in range(1, B + 1):
                string_table.append(a * b)

        string_table = map(str, string_table)
        print(list_to_string(string_table))


list_to_string = lambda string_table: '\t'.join(string_table)

if __name__ == '__main__':
    multiplication_table(2, 3)
    print()
    multiplication_table(9, 9)
