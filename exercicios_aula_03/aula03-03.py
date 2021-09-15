# Faça um programa, com uma função que peça três números, e que
# forneça a soma desses três números.
# ------------------------------------------------------//--------------------------------------------------

# Subprograma
def somaTres(a,b,c):
    soma = a+b+c
    return soma
# Programa Principal
cont = 0
numeros = []
print("Digite 3 números, após cada número tecle [ENTER]\n")
while cont < 3:
    entrada = float(input("Digite o {}º número: ".format(cont+1)))
    numeros.append(entrada)
    cont += 1
print()
print("O resultado da soma é: {:.2f}".format(somaTres(numeros[0],numeros[1],numeros[2])))