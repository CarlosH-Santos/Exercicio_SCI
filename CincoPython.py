#5 - Crie uma matriz bidimensional. Deverá ser solicitado três nomes de alunos e quatro notas, após solicitação dos nomes e das notas deverá ser impresso os nomes acompanhados
# da média geral de cada aluno, deverá ser impresso também o nome do aluno que obteve a maior média e o nome do aluno que obteve a menor média.

matriz = [[], [], []]
posicao_menor_media = 0
posicao_maior_media = 0

for posicao, linha in enumerate(matriz):
    linha.append(input('Digite o nome do aluno: '))

    for i in range(4):
        linha.append(float(input(f'Digite a {i + 1}º nota: ')))

    media = round(sum(linha[1:]) / 4, 2)
    linha.append(media)

    if media > matriz[posicao_maior_media][-1]:
        posicao_maior_media = posicao
    if media < matriz[posicao_menor_media][-1]:
        posicao_menor_media = posicao

for linha in matriz:
    print(f'Aluno {linha[0]} - Média {linha[-1]}')

print(f'Maior média: {matriz[posicao_maior_media][0]}')
print(f'Menor média: {matriz[posicao_menor_media][0]}')

