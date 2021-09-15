# Usando função, faça um programa para imprimir:
#
#     1
#     1 2
#     1 2 3
#     .....
#     1 2 3 ... n
# para hum n Informado cabelo Usuário. Use uma função que receba
# um valor n inteiro imprima até a n-ésima linha.
# ------------------------------------------//-------------------------------------------------------------

# Subprogramas
def printLinha(n):
    for i in range(1, n+1):
        print(str(i)+" ", end='')
    print()
def printNumeros(n):
    for i in range(n + 1):
        printLinha(i)
# Programa Principal
entrada = int(input('Digite um número inteiro: '))
printNumeros(entrada)