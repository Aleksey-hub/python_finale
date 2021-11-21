# Создать два списка с различным количеством элементов. В первом должны быть записаны
# ключи, во втором — значения. Необходимо написать функцию, создающую из данных ключей
# и значений словарь. Если ключу не хватает значения, в словаре для него должно сохраняться
# значение None. Значения, которым не хватило ключей, необходимо отбросить.
def gen_dict(list_keys: list, list_values: list) -> dict:
    dictionary = {}
    for i, key in enumerate(list_keys):
        try:
            dictionary[key] = list_values[i]
        except IndexError:
            dictionary[key] = None
        except TypeError:
            dictionary['error'] = 'list_keys должен состоять из неизменяемых объектов'
            return dictionary

    return dictionary


if __name__ == '__main__':
    list_1 = [1, 2, 3, 4]
    list_2 = ['a', 'b']
    print(gen_dict(list_1, list_2))

    list_1 = [1, 2]
    list_2 = ['a', 'b', 'c']
    print(gen_dict(list_1, list_2))

    list_1 = [[1], 2, 3, 4]
    list_2 = ['a', 'b']
    print(gen_dict(list_1, list_2))
