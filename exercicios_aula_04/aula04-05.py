# Faça um Programa que peça as quatro notas de 10 alunos, calcule
# e armazene num vetor a média de cada aluno, imprima o número
# de alunos com média maior ou igual a 7.0.
from random import randint, uniform
# Subprogramas
def preencheMedia(qtdAluno):
    medias = []
    for indAluno in range(qtdAluno):
        print('Digite a nota do {}º aluno'.format(indAluno+1))
        notas = []
        media = 0
        # entrada = input('Digite as 4 notas do aluno separado por espaço no final tecle [ENTER]: ').split()
        for indNota in range(4):
            # entrada = float(input('Digite a {}ª nota: '.format(indNota+1)))
            entrada = uniform(5.0, 10.0)
            notas.append(round(entrada, 1))
            media += notas[indNota]/4
            print('Notas geradas aleatóriamente!!!')
        medias.append(round(media, 1))
        print('-'*50)
    print('Médias: ',medias)
    return medias
def contaAluno(medias):
    totAlunos = 0
    for indMedias in medias:
        if indMedias >= 7:
            totAlunos += 1
    if totAlunos == 0:
        print('\nQue pena! Ninguém atingiu média maoir ou igual a 7.0')
        exit()
    print('\nMaravilha! {} alunos antigiram média maior ou igual a 7.0.'.format(totAlunos))
# Programa Principal
mediasAlunos = preencheMedia(10)
contaAluno(mediasAlunos)