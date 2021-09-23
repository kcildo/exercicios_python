# Faça um programa que leia duas matrizes 2 x 2 com valores reais.
# Ofereça ao usuário ´ um menu de opções:#
# (a) somar as duas matrizes#
# (b) subtrair a primeira matriz da segunda#
# (c) adicionar uma constante as duas matrizes#
# (d) imprimir as matrizes
#-----------------------------------------//-----------------------------------------------------

# importando o método uniform da biblioteca random para gerar números aleatórios reais com finalidade de teste do programa
from random import uniform
# Subprogramas
#Função para preencher uma matriz 2x2
def preencheMatriz2x2():
    m = []
    for lin in range(2):
        linha = []
        for col in range(2):
            linha.append(float(input(f'Digite o valor da {lin+1}ªlinha e {col+1}ª coluna: ')))
            # linha.append(round(uniform(-20, 20), 2))
        m.append(linha)
    return m
# Função para escrever matrizes
def escreveMatriz(m):
    for lin in range(len(m)):
        for col in range(len(m)):
            print(f'{m[lin][col]:^5}', end=' '*2)
        print()
    print()
# Função para somar matrizes
def somaMatrizes(a, b):
    soma = []
    for lin in range(len(a)):
        linha = []
        for col in range(len(a)):
            linha.append(round((a[lin][col] + b[lin][col]), 2))
        soma.append(linha)
    return soma
# Função para subtrair matrizes
def subtraiMatrizes(a, b):
    soma = []
    for lin in range(len(b)):
        linha = []
        for col in range(len(b)):
            linha.append(round((b[lin][col] - a[lin][col]), 2))
        soma.append(linha)
    return soma
# Função para somar os elementos das matrizes por uma constante
def adicionaConstante(m, n):
    resultado = []
    for lin in range(len(m)):
        somaLinha = []
        for col in range(len(m)):
            somaLinha.append(round((m[lin][col] + n), 2))
        resultado.append(somaLinha)
    return resultado
# Programa Principal
print('-=' *40+'''
Escreva duas matrizes 2x2 e em seguida escolha o que gostaria de fazer
'''+'-=' *40)
# Chamando/ativando a função para preencher matriz 2x2
print('\n Escreva a Matriz A')
matrizA = preencheMatriz2x2()
print('\n Escreva a Matriz B')
matrizB = preencheMatriz2x2()

# Loop para fazer a iteratividade do programa enquanto o usuário quiser
continuar = True
while continuar:
    print('-=' * 40 + '''
    Escolha uma opção abaixo:
    (a) somar as duas matrizes
    (b) subtrair a primeira matriz da segunda
    (c) adicionar uma constante as duas matrizes 
    (d) imprimir as matrizes
    ''' + '-=' * 40)
    escolha = input('Digite a opção desejada: ')
# Validando a entrada para que seja digitado somente as letra válidas para cada opção
    while escolha not in 'AaBbCcDd':
        print('Erro!!! Favor digitar uma opção válida.')
        escolha = input('Digite a opção desejada: ').lower()
# Mediante a escolha do usuário o programa fará o processamento conforme escolha
    if escolha == 'a' or escolha == 'A':
        print('Matriz A + Matriz B: ')
        matrizSoma = somaMatrizes(matrizA, matrizB)
        escreveMatriz(matrizSoma)
    elif escolha == 'b' or escolha == 'B':
        print('Matriz B - Matriz A')
        matrizSubtraida = subtraiMatrizes(matrizA, matrizB)
        escreveMatriz(matrizSubtraida)
    elif escolha == 'c' or escolha == 'C':
        constante = int(input('Digite o valor da constate a ser adicionada as matrizes: '))
        print(f'Matriz A após adição da constante {constante}:')
        addConstante = adicionaConstante(matrizA, constante)
        escreveMatriz(addConstante)
        print(f'Matriz B após adição da constante {constante}:')
        addConstante = adicionaConstante(matrizB, constante)
        escreveMatriz(addConstante)
    elif escolha == 'd' or escolha == 'D':
        print('Matriz A: ')
        escreveMatriz(matrizA)
        print('Matriz B: ')
        escreveMatriz(matrizB)
    decisao = input('Deseja escolher outra opção? [S/N]: ').upper()
    while decisao not in 'SsNn':
        print('Erro! Favor digitar uma opção válida')
        decisao = input('Deseja escolher outra opção? [S/N]: ').upper()
    if decisao == 'N':
        print('Obrigado! :)')
        continuar = False
