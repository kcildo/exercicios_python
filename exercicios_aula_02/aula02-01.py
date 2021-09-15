# Faça um Programa que peça dois números, imprima
# o maior deles e diga se ele é par ou impar.#
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
while num1 == num2:
    print('\nOs números são iguais, favor digitar números diferentes!!!')
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    maior = num1
else:
    maior = num2
print('\nO maior valor digitado foi %4.2f' % (maior), end=' e ele é ')
if maior % 2 == 0:
    print('PAR')
else:
    print('ÍMPAR')

