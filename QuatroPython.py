#4- Criar um vetor de cinco posições, solicitar  cinco números e ao fim, imprimir o valor apresentado na posição três.

lista = []

for i in range(5):
    lista.append(float(input('Digite o número: ')))

print(f'Na posição 3 está o número: {lista[2]:.0f}')
