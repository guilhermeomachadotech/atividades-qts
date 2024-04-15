#07) Faça um prograja que apresente os elementos de uma tupla a partir de uma posição específica.
#Posição 5-8, posição 2- até o final, penúltima e última posição, posição 3-15, posição 10-12

tupla = (2000, 300, True, '312N', '555', 89, 1990, 300, 'São Paulo apital', 2023, 257, 999, 654, 712, 'Estação Itaquera', False, 400, 221, 'Estação Guaianazes')

print('Tupla Original: ', tupla)
print('Intervalo da posição 5 a 8: ', tupla[4:7])
print('Intervalo da posição 2 até o final: ', tupla[1:-1])
print('Intervalo da penúltima e última posição: ', tupla[(len(tupla)-2):(len(tupla))])
print('Intervalo da posição 3 a 15: ', tupla[2:14])
print('Intervalo da posição 10 a 12: ', tupla[9:11])