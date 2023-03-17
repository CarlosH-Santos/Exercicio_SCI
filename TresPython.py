#3- Elabore um programa de computador que realize o cálculo de notas. Este programa deverá solicitar o nome do aluno e quatro notas,
# todo este conjunto deverá estar contido em um laço que confirme se deseja encerrar o programa ou continuar solicitando outros nomes e notas.
# Ao final da solicitação do nome e das notas deverá ser impresso o nome do aluno e a sua média, se a nota for  menor que 6 imprimir Reprovado,
# senão, se a nota for igual ou maior que 6, imprimir Aprovado.

notas = {}

while True:

    nome_aluno = str(input('Digite o seu nome: '))
    notas[nome_aluno] = {'notas': []}

    for n in range(4):
        notas[nome_aluno]['notas'].append(float(input(f'Digite a {n + 1}º nota: ')))

    notas[nome_aluno]['media_notas'] = sum(notas[nome_aluno]['notas']) / 4

    continuar = str(input('Deseja continuar?[S/N]: ')).upper()
    if continuar == 'N':
        break

for aluno in notas.keys():
    print(f'Aluno {aluno} {"Aprovado" if notas[aluno]["media_notas"] > 6 else "Reprovado"}')