#Exercicio_02 - Solicitar 5 números, ao fim, imprimir o número maior e o número menor.

print('DIGITE 5 NUMEROS!')

lista = []
for n in range(5):
    num = float(input('Digite um numero: '))
    lista.append(num)

print(f'O maior numero digitado foi: {max(lista)}')
print(f'O menor numero digitado foi: {min(lista)}')
