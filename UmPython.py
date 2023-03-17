#Exercício 01 - Solicitar a inserção de 5 números, ao final, imprimir os números pares, números ímpares e a média geral desses números.

lista = []
lista_pares = []
lista_impares = []

print('Digite 5 números!')

for n in range(5):
    lista.append(int(input('Numero: ')))

for n in lista:
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)

media = sum(lista) / len(lista)

print(f'Média geral: {media:.2f}')
print(f'Os numeros pares são: {lista_pares}')
print(f'Os numeros impares são: {lista_impares}')

