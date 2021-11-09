# Faça um programa que leia uma matriz 4 x 4,
# conte e escreva quantos valores maiores que 10 ela possui.
from random import randint #importando randint da biblioteca random para gerar números aleatórios
print('Informe valores inteiros para formar uma matriz 4x4')
matriz = []
cont = 0
for lin in range(4): # loop para preencher as colunas da matriz
    linha = [] # declarando o vetor linha, a mesma será zerada ao final de cada cliclo de 4 colunas por linha para preencher a próxima linha
    for col in range(4): # loop para preencher as linhas da matriz
        linha.append(int(input('Digite o valor da {}ª linha e {}ª coluna: '.format(col+1,lin+1)))) # recebendo valor da entrada padrão e inserindo no vetor linha para preencher a linha da matriz
        # linha.append(randint(0,25)) # gerando valores aleatórios para preenhcer as linhas automaticamente com inteiros de 0 a 25
        if linha[col] > 10: # condicional para verificar se o número inserido na linha é maior que 10
            cont += 1 # variável para contar dos números maiores que 10
    matriz.append(linha) #adicionando o vetor linha na matriz
print('A matriz digitada foi:\n')
# imprimindo em formato de matriz
for ind in range(len(matriz)):
    print(matriz[ind])
print('\nExistem {} números maior que 10!'.format(cont))
