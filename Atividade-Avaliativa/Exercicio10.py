#10)Faça um programa que distribuía os valores de uma tupla em variáveis individuais “Unpacking”
timesFutebol = ("Real Madrid", "Barcelona", "Manchester City", "Liverpool", "Bayern de Nunique", "Paris Saint-Germain", "Chelsea",  "Juventus", "Burussia", "Dortmund", "Atlético de Madrid")
print('Times na Tupla: ', timesFutebol)

realMadrid, barcelona, manchesterCity, liverpool, bayern, psg, chelsea, juventus, borussia, dortmund, atleticoMadrid = timesFutebol

print('Times Separados:')

print('#'*40)

print("Real Madrid:", realMadrid)
print("Barcelona:", barcelona)
print("Manchester City:", manchesterCity)
print("Liverpool:", liverpool)
print("Bayern de Munique:", bayern)
print("Paris Saint-Germain:", psg)
print("Chelsea:", chelsea)
print("Juventus:", juventus)
print("Borussia:", borussia)
print("Dortmund:", dortmund)
print("Atlético de Madrid:", atleticoMadrid)