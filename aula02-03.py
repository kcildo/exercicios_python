# Faça um programa que pergunte o preço de três produtos e
# informe qual produto você deve comprar, sabendo que a decisão é
# sempre pelo mais barato.

# declarando variáveis recebendo valores digitados
prod1 = float(input('Digite o valor do 1º produto: '))
prod2 = float(input('Digite o valor do 2º produto: '))
prod3 = float(input('Digite o valor do 3º produto: '))
# tratando as entradas para que não aja valores iguais
while (prod1 == prod2) or (prod2 == prod3) or (prod3 == prod1):
    print('\nFAVOR NÃO DIGITAR VALORES IGUAIS!!\n')
    prod1 = float(input('Digite o valor do 1º produto: '))
    prod2 = float(input('Digite o valor do 2º produto: '))
    prod3 = float(input('Digite o valor do 3º produto: '))
# Verificando o produto mais barato
if (prod1 < prod2) and (prod1 < prod3):
    print('\nVocê deve comprar o [1º PRODUTO]! Está bem mais em conta.')  # Imprimindo na saída padrão
elif (prod2 < prod1) and (prod2 < prod3):
    print('\nVocê deve comprar o [2º PRODUTO]! Está bem mais em conta.')  # Imprimindo na saída padrão
else:
    print('\nVocê deve comprar o [3º PRODUTO]! Está bem mais em conta.')  # Imprimindo na saída padrão