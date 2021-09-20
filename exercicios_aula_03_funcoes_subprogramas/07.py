# Faça um programa que use a função valorPagamento para determinar
# o valor a ser pago por uma prestação de uma conta.
#
# O programa deverá solicitar ao usuário o valor da prestação e o
# número de dias em atraso e passar estes valores para a função
# valorPagamento, que calculará o valor a ser pago e devolverá este
# valor ao programa que a chamou.
#
# O programa deverá então exibir o valor a ser pago na tela. Após a
# execução o programa deverá voltar a pedir outro valor de prestação
# e assim continuar até que seja informado um valor igual a zero para
# a prestação.
#
# Neste momento o programa deverá ser encerrado, exibindo o
# relatório do dia, que conterá a quantidade e o valor total de
# prestações pagas no dia.
#
# O cálculo do valor a ser pago é feito da seguinte forma.
#
# Para pagamentos sem atraso, cobrar o valor da prestação.
#
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
# ------------------------------------------------------------//-----------------------------------------------------

# Suprograma
def valorPagamento(prestacao, dias):
    encargos = 0.031  # soma dos encargos por dia 3% + 0,1% = 3,1% = 0,031
    totalEncargos = (encargos * prestacao) * dias  # Cálculo total dos encargos pagos

    if dias == 0:
        print('PARABÉNS não houve atraso!!!')
        return prestacao, totalEncargos  # Retonando o valor da prestação sem encargos e total de encagos, que nesse caso será = 0

    elif dias > 0:
        novaPrestacao = (encargos * dias) * prestacao + prestacao  # Cálculo da nova prestação depois dos encargos
        return novaPrestacao, totalEncargos  # Retronando o valor da prestação com encargos e o total de encargos pagos


# Programa Principal
print('Cálculo de encargos sobre valor de prestação em atraso.\n')

quant = somaPrestacao = somaEncargos = 0  # Iniciando variáveis

valorPrestacao = float(
    input("\nDigite o valor da prestação: R$ "))  # iniciando variável recebendo valor de entrada padrão

while valorPrestacao <= 0:  # Iniciando loop para validar entrada para que seja maior que 0
    print('''ERRO! VALOR INICIAL NÃO PODE SER MENOR OU IGUAL A [0]. 
FAVOR INFORME OUTRO VALOR OU [0] PARA FINALIZAR.''')  # Informação ao usuária em caso de erro.
    valorPrestacao = float(input("\nDigite o valor da prestação: R$ "))  # Pedindo novo valor ao usuário em caso de erro
    if valorPrestacao == 0:  # Condição para FINALIZAR a execução do programa como informado ao usuário
        print('OBRIGADO PELA PREFERÊNCIA!')
        exit()  # Finalizando a execução do programa

while valorPrestacao > 0:  # Condição de parada do loop em caso de valorPrestacao = ou menor que 0
    quant += 1  # Atualiza valor da variável quant adicionando mais 1 ao seu valor
    numDiasAtraso = int(input("\nDigite o número de dias em atraso: "))
    prestacao, totalEncargos = valorPagamento(valorPrestacao,
                                              numDiasAtraso)  # variáveis para chamar a função e armazenar os valores retornados

    print('\nValor da prestação a ser pago R$ {0:.2f} sendo R$ {1:.2f} de encargos'.format(prestacao,
                                                                                           totalEncargos))  # Imprimindo na saída padrão
    print('-' * 50)  # Imprimindo separador na saída padrão

    somaPrestacao += prestacao  # variável para fazer o somatório das prestações informadas
    somaEncargos += totalEncargos  # variável para fazer o somatório dos encargos cobrado sobre as prestações em atraso

    print('\nPara finzalizar digite [0] como valor da prestação!')
    valorPrestacao = float(input(
        "\nDigite o valor da prestação: R$ "))  # Atualizando valor da variável valorPrestacao caso seja informado 0 encerra o loop

print('''
Total de prestações pagas: {0:d}
Valor total de prestações pagas: R$ {1:.2f}
Valor total de encargos: R$ {2:.2f}
'''.format(quant, somaPrestacao, somaEncargos))  # Impressão de relatório final conforme solicitado
