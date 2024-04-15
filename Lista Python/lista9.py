#Escreva um programa que leia uma lista(10 valores) de números inteiros e imprima a média dos números da lista. Mais uma vez os valores devem ser digitados pelo usuário.
lista1=[];
media=0
for i in range (1,10):
     lista1.append(int(input('digite o primeiro valor:')))
media=(sum(lista1))/10

print(lista1)
print('Média: ')
print(media)