# Faça um programa que mostre todos os primos entre 1 e N sendo N
# um número inteiro fornecido pelo usuário. O programa deverá
# mostrar também o número de divisões que ele executou para
# encontrar os números primos. Serão avaliados o funcionamento,
# o estilo e o número de testes (divisões) executados.

#declarando variável recebendo valor da entrada padrão
n = int(input('Digite um número inteiro: '))
quantDiv = 0 #inciando variável
print('Os números primos de 1 a {} são: '.format(n))
#fazendo loop com for dentro de for para dividir os números do intervalo.
for i in range(1, n+1):
    for c in range(2, i):
        if i % c == 0:
            break
    else:
        print(i,end=' ')
        quantDiv +=1
print('.Foram realizadas {} divisões'.format(quantDiv))