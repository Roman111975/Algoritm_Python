"""
1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья
прибыль выше среднего и отдельно вывести наименования предприятий,
чья прибыль ниже среднего.

"""
from collections import namedtuple

firm = namedtuple("firm", "name q1 q2 q3 q4")

count = int(input("Введите количество предприятий: "))

firm_list = []
for i in range(count):
    quart_money = []
    quart_name = str(input("Введите название компании #%d: " % (i + 1)))
    for quart in range(4):
        quart_money.append(float(input("Введите прибыль компании #%d за %d квартал:" % (i + 1, quart + 1))))
    firm_list.append(firm(quart_name, *quart_money))

avg_profit = 0
for info in firm_list:
    avg_profit += info.q1 + info.q2 + info.q3 + info.q4
avg_profit /= count
print("Средняя прибыль за год для всех: %.2f" % avg_profit)


def count_firm_profit(info):
    return info.q1 + info.q2 + info.q3 + info.q4


print("Компании с прибылью выше средней:")
[print(info.name + ":", str(count_firm_profit(info))) for info in firm_list if count_firm_profit(info) >= avg_profit]

print("Компании с прибылью ниже средней:")
[print(info.name + ":", str(count_firm_profit(info))) for info in firm_list if count_firm_profit(info) < avg_profit]