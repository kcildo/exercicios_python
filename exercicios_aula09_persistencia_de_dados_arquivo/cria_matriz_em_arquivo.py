# Subprogramas
def criaMatriz(cont):
    from random import randint
    m = []
    qtdlin = int(input(f'Digite o número de linhas que a {cont+1}ª matriz terá: '))
    qtdCol = int(input(f'Digite o número de colunas que a {cont+1}ª matriz terá: '))
    for lin in range(qtdlin):
        linha = []
        for col in range(qtdCol):
            linha.append(randint(-5, 20))
        m.append(linha)
    return m, qtdlin
def imprimeMatriz(m):
    for lin in m:
        for col in lin:
            print(f'{col:^3}', end=' ' * 2)
        print()
def escreveArquivo(m, qtdLin):
    # arquivo = open('testeAD2Q1.txt', 'w')
    with open('testeAD2Q1.txt', 'a') as arquivo:
        arquivo.write(str(qtdLin) + '\n')
        for lin in m:
            for col in lin:
                arquivo.write(f'{str(col):^3}'+' '*2)
            arquivo.write('\n')
    # arquivo.close()
# Programa principal
qtdMatriz = int(input('Digite quantas matrizes deseja criar em arquivo: '))
cont = 0
while cont < qtdMatriz:
    matriz, qtdLin = criaMatriz(cont)
    imprimeMatriz(matriz)
    cont += 1
    escreveArquivo(matriz, qtdLin)

