#12) Remova o time da posição 5 da tupla a seguir:
timesFutebol = ("Real Madrid", "Barcelona", "Manchester City", "Liverpool", "Bayern de Nunique", "Paris Saint-Germain", "Chelsea",  "Juventus", "Burussia", "Dortmund", "Atlético de Madrid")
print(timesFutebol)
timesFutebol_sem_posicao_5 = timesFutebol[:4] + timesFutebol[5:]
print(timesFutebol_sem_posicao_5)