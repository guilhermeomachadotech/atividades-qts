#Escreva um programa que leia uma lista(10 valores) de números inteiros e imprima a soma de todos os números pares da lista. A entrada dos valores deve ser informada pelo usuário.
lista1=[];
listaPar=[];
for i in range (1,10):
    lista1.append(int(input('Digite o valor do indice ')))
for i in lista1:
    if i%2==0:
        listaPar.append(i);
print(lista1)
print('Quantidade de Números Pares no Array:')
print(sum(listaPar));

