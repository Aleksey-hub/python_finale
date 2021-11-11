# Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна
# передаваться фиксированная ежемесячная сумма пополнения вклада. Необходимо в главной
# функции реализовать вложенную функцию подсчета процентов для пополняемой суммы.
# Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и
# последнего. Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4
# месяцев. Вложенная функция возвращает сумму дополнительно внесенных средств (с
# процентами), а главная функция — общую сумму по вкладу на конец периода.
from typing import Union


def final_deposit_sum(sum_deposit: Union[int, float], month_deposite: int,
                      monthly_deposit_add: Union[int, float]) -> float:
    def final_additional_sum() -> float:
        final_additional_sum = 0
        for month in range(2, month_deposite):
            final_additional_sum += (final_additional_sum * current_interest_rate / 12) / 100
            final_additional_sum += monthly_deposit_add
        return final_additional_sum

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

    return final_additional_sum() + sum_deposit + (sum_deposit * current_interest_rate * month_deposite / 12) / 100


if __name__ == '__main__':
    print(final_deposit_sum(1000, 6, 100))
