#13) Remova os seguintes times da tupla "timesFutebol": Real Madrid e Juventus.
timesFutebol = ("Real Madrid", "Barcelona", "Manchester City", "Liverpool", "Bayern de Nunique", "Paris Saint-Germain", "Chelsea",  "Juventus", "Burussia", "Dortmund", "Atlético de Madrid")
timesFutebolsemRealJuventus = timesFutebol[1:7]+timesFutebol[8:-1]
print(timesFutebolsemRealJuventus)