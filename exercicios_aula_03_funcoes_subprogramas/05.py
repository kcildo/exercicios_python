# Faça um programa com uma função chamada somaImposto.
# A função possui dois parâmetros formais: taxaImposto, que é a
# quantia de imposto sobre vendas expressa em porcentagem e custo,
# que é o custo de um item antes do imposto. A função “altera” o valor
# de custo para incluir o imposto sobre vendas.
# ------------------------------------------------------------//-----------------------------------------------------

# Subprograma
def somaImposto(taxaImposto, custo):
    resultado = custo * taxaImposto + custo
    return resultado
# Progama Principal
print('Calcule o valor de um item com taxação do imposto sobre vendas\n')
print('''Digite o valor em dicmal como no Exemplo abaixo: 
0.05 = 5%
0.10 = 10%
0.15 = 15%
0.50 = 50%
1.0 = 100%
''')
imposto = float(input('Digite do imposto a ser cobrado: '))
while (imposto <= 0) or (imposto > 1.0): # Valída para que imposto esteja entre 0 e 1.0
    if (imposto <= 0):
        print('\nERRO! Imposto não pode ser menor ou igual a [0]. FAVOR DIGITE OUTRO VALOR!')
        imposto = float(input('Digite o valor em dicmal do imposto a ser cobrado: '))
    elif (imposto > 1.0):
        print('\nERRO! Imposto não pode ser maior que [1.0], ou seja 100%. FAVOR DIGITE OUTRO VALOR!')
        imposto = float(input('Digite o valor em dicmal do imposto a ser cobrado: '))
entrada = float(input("\nDigite o custo do item R$ "))
while entrada <=0:
    print('\nERRO! Custo do item não pode ser menor ou igual a [0]. FAVOR DIGITE OUTRO VALOR!')
    entrada = float(input("Digite o valor do item R$ "))
print('\nO novo custo após a taxação sobre vendas é de R$ %.2f'%somaImposto(imposto,entrada)) # Chama a função somaImposto passando os parametros)



