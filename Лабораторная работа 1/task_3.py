list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
number_of_players = len(list_players)
teem_1 = list_players[:round(number_of_players/2)]
teem_2 = list_players[round(number_of_players/2):]
print(teem_1)
print(teem_2)