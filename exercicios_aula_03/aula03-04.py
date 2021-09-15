# Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’, se seu argumento for
# positivo, e ‘N’, se seu argumento for zero ou negativo.
# -----------------------------------------------------------//---------------------------------------------

# Subprograma
def verificaPositivoNegativo(n):
    if n > 0:
        return 'P'
    else:
        return 'N'
# Programa Principal
entrada = float(input("Informe um número: "))
print('\n',verificaPositivoNegativo(entrada))