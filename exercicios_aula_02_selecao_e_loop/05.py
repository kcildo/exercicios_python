# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

#declaração de variável recebendo valor da entrada padrão
nota = float(input('Digite uma nota entre [0] e [10]: '))
#loop para verificar se nota é < 0 ou > 10
while nota < 0 or nota > 10:
    print('\nVALOR INVÁLIDO!\n')
    nota = float(input('Digite uma nota entre [0] e [10]: '))