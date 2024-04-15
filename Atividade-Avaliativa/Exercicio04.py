#04) Escreva um programa que receba duas tuplas de números e retorne uma nova tupla com a soma dos elementos correspondentes das duas tuplas.
tupla1 = (200, 400, 60000, 90000, 13, 27, 93, 100, 205)
tupla2 = (1900, 2026, 1041, 290, 97, 88, 23, 22, 1)
print('Tupla 1 Original: ', tupla1)
print('Tupla 2 Original', tupla2)
print('Soma Tupla 1: ', sum(tupla1))
print('Soma Tupla 2: ', sum(tupla2))
tupla3 = ((sum(tupla1)+sum(tupla2)))
print('Soma dos elementos das tuplas: ', tupla3)