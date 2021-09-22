# Faça uma matriz 4 x 4
## Leia a matriz.
# Imprima a matriz e retorne a localização (linha e a coluna) do maior valor.
#--------------------------------------------------------//-------------------------------------------------------

from random import randint  # importando o método randint da biblioteca random para gerar números inteiros aleatórios
#Subprogramas
def preencheMatriz():  # função para preencher uma matriz 4x4
    m = []
    for lin in range(4):
        linha = []
        for col in range(4):
            # linha.append(int(input('Digite o valor da {}ª linha e {}ª coluna: '.format(lin+1,col+1))))
            linha.append(randint(0, 50))
        m.append(linha)
    return m
def escreveMatriz(m): # Função para escrever a matriz na saída padrão
    print('\nMatriz obtida:')
    for ind in range(len(m)):
        print(m[ind])
def procuraMaior(m): # Função para veriricar o maio número e retornar sua posição
    maior = linha = coluna = 0
    for lin in range(len(m)):
        for col in range(len(m)):
            if m[lin][col] > maior:
                maior = m[lin][col]
                linha = lin
                coluna = col
    return maior, linha, coluna
# Programa Principal
print('''-----------------------------------------------------------------------------------------------------
Programa para preencher uma matriz 4x4 escrever a mesma na tela,
descobrir o maior valor da matriz, e retornar a posição do mesmo dentro
da matriz.
--------------------------------------------------------------------------------------------------------''')
matriz = preencheMatriz()
escreveMatriz(matriz)
maior, linha, coluna = procuraMaior(matriz)
print('\nO maior valor da matriz é {} e está localizado na {}ª linha e {}ª coluna'.format(maior, linha + 1, coluna + 1))



