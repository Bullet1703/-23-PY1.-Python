money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
mounth = 0
dolg = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while money_capital > 0:
    mounth += 1
    spend += (spend*increase)
    dolg = spend-salary
    money_capital -= dolg


print("Количество месяцев, которое можно протянуть без долгов:", mounth )
