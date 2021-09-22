# Leia uma matriz 5 x 3 com as notas de 6 alunos em 3 provas.
# Em seguida, escreva o numero de alunos cuja pior nota foi na prova 1,
# a quantidade de alunos cuja pior nota foi na prova 2, e a quantidade
# de alunos cuja pior nota foi na prova 3.
# ------------------------------------------------\\-------------------------------------------------------

from random import uniform
# Subprogramas
def preencheMatriz(): # Função para preencher matriz 6x3 reprensentando 6 alunos e 3 notas  por coluna de cada linha
    m = []
    for aluno in range(6):
        notas = []
        for nota in range(3):
            notas.append(float(input('Digite a {}ª nota do aluno {}:  '.format(nota+1, aluno+1))))
            # notas.append(round(uniform(4.0,10.0),1)) # adicionando números reais aleatórios utilizando o método uniform com uma casa decimal utilizando o método round
        m.append(notas)
    return m
def escreveMatriz(m): # escreve a matriz na tela
    print('\nAs notas dos alunos foram: ')
    for ind in range(len(m)):
        print('Aluno',ind+1, m[ind])
    print()
def contaMenor(m): # procura o menor de cada linha e a posição que o mesmo está contando a quantidade de pior nota em cada coluna de cada linha
    pos = cont1 = cont2 = cont3 = 0
    for aluno in range(len(m)):
        menor = 10
        for nota in range(3):
            if m[aluno][nota] < menor:
                menor = m[aluno][nota]
                pos = nota
        print('A menor nota do aluno {} foi {} na {}ª prova'.format(aluno + 1, menor, pos + 1))
        if pos == 0:
            cont1 += 1
        elif pos == 1:
            cont2 += 1
        else:
            cont3 += 1
    return cont1, cont2, cont3
# Programa Principal
print('''-----------------------------------------------------------------------------
Programa para verificar a menor nota de 3 provas
informadas de 6 alunos distintos
-----------------------------------------------------------------------------''')
matriz = preencheMatriz()
escreveMatriz(matriz)
cont1, cont2, cont3 = contaMenor(matriz)
print('''
{} aluno(s) tiraram sua pior nota na 1ª prova
{} aluno(s) tiraram sua pior nota na 2ª prova
{} aluno(s) tiraram sua pior nota na 3ª prova
'''.format(cont1, cont2, cont3))
