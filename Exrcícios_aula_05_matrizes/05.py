# Faça um programa que permita ao usuário criar uma matriz de 3 x 3 números inteiros.
#  Em seguida, gere um array unidimensional pela soma dos números de cada  coluna da matriz e mostrar na tela esse array.
# #Por exemplo, a matriz:
#    5   -8  10
#   1    2  15
#  25  10    7
# Vai gerar um vetor, onde cada posição e a soma das colunas da matriz. A primeira  posição ser á 5 + 1 + 25, e assim por diante:
# 31 4 3
#----------------------------------------------------------------------------------//--------------------------------------------------------------------------------------------
# importando o método randint da biblioteca random para
# gerar números inteiros aleatórios para usar em testes
from random import randint
# Subprogramas
# Função para preencher uma Matriz 3x3 com valores digitados pelo usuário
def preencheMatriz3x3():
    m = []
    for lin in range(3):
        linha = []
        for col in range(3):
            linha.append(int(input('Digite o valor da {}ª linha e {}ª coluna: '.format(lin+1, col+1))))
# adicionanado números inteiros aleatórios na linha da matriz,
# utilizada somente para testes do programa
            # linha.append(randint(-20, 50))
        m.append(linha)
    print('-=' * 30)
# Retornando a matriz para o programa principal
    return m
# Função para escrever na saída padrão a matriz informada pelo usuário
def escreveMatriz(m):
    print('Matriz informada: ')
    for lin in range(len(m)):
        for col in range(len(m)):
            print(f'{m[lin][col]:^5}', end=' '*2)
        print()
# Função para somar cada coluna da matriz e guarda no vetor resultado
def somaColuna(m):
    resultado = []
    for ind in range(len(m)):
        soma = 0
        for col in range(len(m)):
            soma += m[col][ind]
        resultado.append(soma)
# Retornando o vetor resultado para o programa principal
    return resultado
# Programa Principal
print('-='*35+'''
Informe uma Matriz 3x3 para calcular a soma de cada coluna
como resultado será informado um vetor com a soma de cada
coluna.
'''+'-='*35)
matriz = preencheMatriz3x3()
escreveMatriz(matriz)
vetorSoma = somaColuna(matriz)
print('A soma de cada coluna é: ')
# Imprimindo na saída padrão o vetor com as comas de cada coluna
# da matriz informada pelo usuário
for i in range(len(vetorSoma)):
    print(f'{vetorSoma[i]:^5}', end=' ')
