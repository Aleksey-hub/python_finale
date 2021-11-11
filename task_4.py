# Написать программу «Банковский депозит». Она должна состоять из функции и ее вызова с
# аргументами. Клиент банка делает депозит на определенный срок. В зависимости от суммы и
# срока вклада определяется процентная ставка: 1000–10000 руб (6 месяцев — 5 % годовых,
# год — 6 % годовых, 2 года — 5 % годовых). 10000–100000 руб (6 месяцев — 6 % годовых, год
# — 7 % годовых, 2 года – 6.5 % годовых). 100000–1000000 руб (6 месяцев — 7 % годовых, год
# — 8 % годовых, 2 года — 7.5 % годовых). Необходимо написать функцию, в которую будут
# передаваться параметры: сумма вклада и срок вклада. Каждый из трех банковских продуктов
# должен быть представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24). Ключам
# соответствуют значения начала и конца диапазона суммы вклада и значения процентной
# ставки для каждого срока. В функции необходимо проверять принадлежность суммы вклада к
# одному из диапазонов и выполнять расчет по нужной процентной ставке. Функция возвращает
# сумму вклада на конец срока.
from typing import Union


def final_deposit_sum(sum_deposit: Union[int, float], month_deposite: int) -> float:
    deposit_1 = {'begin_sum': 1000,
                 'end_sum': 10000,
                 6: 5,
                 12: 6,
                 24: 5}
    deposit_2 = {'begin_sum': 10000,
                 'end_sum': 100000,
                 6: 6,
                 12: 7,
                 24: 6.5}
    deposit_3 = {'begin_sum': 100000,
                 'end_sum': 1000000,
                 6: 7,
                 12: 8,
                 24: 7.5}

    if sum_deposit < deposit_1['end_sum'] and sum_deposit >= deposit_1['begin_sum']:
        current_deposit = deposit_1
    elif sum_deposit < deposit_2['end_sum'] and sum_deposit >= deposit_2['begin_sum']:
        current_deposit = deposit_2
    elif sum_deposit < deposit_3['end_sum'] and sum_deposit >= deposit_3['begin_sum']:
        current_deposit = deposit_3

    if month_deposite == 6:
        current_interest_rate = current_deposit[6]
    elif month_deposite == 12:
        current_interest_rate = current_deposit[12]
    elif month_deposite == 24:
        current_interest_rate = current_deposit[24]

    return sum_deposit + (sum_deposit * current_interest_rate * month_deposite / 12) / 100


if __name__ == '__main__':
    print(final_deposit_sum(1000, 6))
