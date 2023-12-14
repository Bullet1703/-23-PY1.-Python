salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
cloud = spend-salary
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(9):
    spend += (spend*increase)
    if (salary-spend) < 0:
        cloud += spend-salary


print("Подушка безопасности, чтобы протянуть",months ,"месяцев без долгов:", round(cloud, 2))
