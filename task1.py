"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""


def company_less_average_profit(copany, average_profit):
    for company_fild in company._fields:
        copany_profit = getattr(company, company_fild)
        if sum(copany_profit) < average_profit:
            print(
                f'Предприятие {company_fild} прибыль за каждый квартал (Всего 4 квартала) {" ".join(map(str, copany_profit))} прибыль за год {sum(copany_profit)}')


def company_more_average_profit(copany, average_profit):
    for company_fild in company._fields:
        copany_profit = getattr(company, company_fild)
        if sum(copany_profit) >= average_profit:
            print(
                f'Предприятие {company_fild} прибыль за каждый квартал (Всего 4 квартала) {" ".join(map(str, copany_profit))} прибыль за год {sum(copany_profit)}')


import collections

count_company = int(input('Введите количество предприятий: '))
name_company = []
profit_val = []
for num in range(count_company):
    profit_cm = []
    name_company.append(input(f'Введите наименование компании {num + 1}: '))
    for num_quarter in range(4):
        profit_cm.append(int(input(f'Введите прибыль за {num_quarter + 1} квартал: ')))
    profit_val.append(profit_cm)
company = collections.namedtuple('profit_val', name_company)._make(profit_val)
total_profit = 0
for company_fild in company._fields:
    company_profit = getattr(company, company_fild)
    total_profit += sum(company_profit)
    print(
        f'У предприятия {company_fild} прибыль за каждый квартал (Всего 4 квартала) {" ".join(map(str, company_profit))} прибыль за год {sum(company_profit)}')
print('_' * 100)
print(f'Общая прибыль всех предприятий {total_profit}')
average_profit = total_profit / len(company)
print(f'Средняя прибыль всех предприятий {average_profit}')
print('_' * 100)
print(f'Список компаний с прибылью больще или равна средней {average_profit}')
company_more_average_profit(company, average_profit)
print('_' * 100)
print(f'Список компаний с прибылью меньше средней {average_profit}')
company_less_average_profit(company, average_profit)
