# Usando função, faça um programa para imprimir:
#
#     1
#     2 2
#     3 3 3
#     .....
#     nnnnnn ... n
#
# para um  n  Informado pelo Usuário. Use uma função que receba
# um valor  n  inteiro e imprima até a n-ésima linha.
#
# Observe que no exemplo, se digitado 3, imprimiria apenas até 3 3 3.
#---------------------------------------------//-----------------------------------------------------------------

# Subprograma
def printQdt(n): # criando a função printQdt
    for i in range(1,n+1):
        qdtPrint = n - n + i
        print((str(qdtPrint)+" ")*i,) # Imprimindo conforme solicitado
# Programa Principal
entrada = int(input("Digite um número inteiro: "))
printQdt(entrada) # Chamando a função passando entrada como parâmetro