list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
middle_index=len(list_players)//2
team1= list_players[:middle_index]
team2=list_players[middle_index:]
print(team1)
print(team2)