# Faça um Programa que peça os 3 lados de um triângulo. O programa
# deverá informar se os valores podem ser um triângulo. Indique, caso
# os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois
# lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

# declaração de variáveis recebendo valor da entrada padrão
lado1 = float(input('Digite o 1º lado: '))
lado2 = float(input('Digite o 2º lado: '))
lado3 = float(input('Digite o 3º lado: '))

# Utilização do if, elif e else para seleção e verificação de condições
if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado3 + lado1 > lado2):
    # imprimindo na saída padrão com end para que o próximo print fique na mesma linha
    print('\nOs tamanhos de lados informados podem\nformar um triângulo do tipo:', end='')

    # verificando o tipo de triângulo com if, elif e else
    if (lado1 == lado2 == lado3):
        # imprimindo na saída padrão
        print(' [Equilátero]')
    elif (lado1 == lado2) or (lado2 == lado3) or (lado3 == lado1):
        # imprimindo na saída padrão
        print(' [Isósceles]')
    else:
        # imprimindo na saída padrão
        print(' [Escaleno]')

# caso as condições não sejam verdadeiras
else:
    # imprimindo na saída padrão
    print('\nOs tamanhos de lados informados não podem formar um triângulo.')