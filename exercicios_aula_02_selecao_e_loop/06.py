# As Organizações Tabajara resolveram dar um aumento de salário
# aos seus colaboradores e lhe contraram para desenvolver o programa
# que calculará os reajustes.
#
# Faça um programa que recebe o salário de um colaborador e o
# reajuste segundo o seguinte critério, baseado no salário atual:
#
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

#declaração de variável recebendo valores da entrada padrão
salAtual = float(input('Digite o valor do salário do colaborador: R$'))

# utilizando if e elif para selecinar a faixa salarial e fazer o cálculo de aumento
if salAtual <= 280:
    aumento = salAtual * 0.2
    salNovo = aumento + salAtual
#imprimindo na saída padrão
    print('''\nO colaborador recebe R${0:.2f}. Após o acrésimo de 20% sobre o 
seu salário, ou seja R${1:.2f}, seu novo salário será de R${2:.2f}.'''.format(salAtual,aumento,salNovo))

elif (salAtual > 280) and (salAtual <= 700):
    aumento = salAtual * 0.15
    salNovo = aumento + salAtual
#imprimindo na saída padrão
    print('''\nO colaborador recebe R${0:.2f}. Após o acrésimo de 15% sobre o
seu salário, ou seja R${1:.2f}, seu novo salário será de R${2:.2f}.'''.format(salAtual,aumento,salNovo))

elif (salAtual > 700) and (salAtual <= 1500):
    aumento = salAtual * 0.1
    salNovo = aumento + salAtual
#imprimindo na saída padrão
    print('''\nO colaborador recebe R${0:.2f}. Após o acrésimo de 10% sobre o
seu salário, ou seja R${1:.2f}, seu novo salário será de R${2:.2f}.'''.format(salAtual,aumento,salNovo))

else:
    aumento = salAtual * 0.05
    salNovo = aumento + salAtual
#imprimindo na saída padrão
    print('''\nO colaborador recebe R${0:.2f}. Após o acrésimo de 5% sobre o
seu salário, ou seja R${1:.2f}, seu novo salário será de R${2:.2f}.'''.format(salAtual,aumento,salNovo))