# Crie uma matriz 5 x 5.
#  Preencha com 1 a diagonal principal e com 0 os demais elementos.
#  Escreva ao final a matriz obtida.
print('''Colocando o número um [1] na diagonal de uma matriz
5x5 de zeros [0].

Matriz obtida:''') # imprimindo na saída padrão considerando as quebras de linhas dentro do print
matriz = []
for col in range(5):
    linha = []
    for lin in range(5):
        if col == lin:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)
    print(matriz[col])