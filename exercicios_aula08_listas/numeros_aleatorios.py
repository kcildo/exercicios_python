# Criando uma lista de números com quantidade de números
# aleatórios e um intervalo de valores escolhidos pelo usuário.
# Subprogramas
def preencher(listaElems, qtd, min, max):
    from random import randint
    for item in range(qtd):
        listaElems.append(randint(min,max))
    return None
# Programa Principal
qtdNumeros = int(input('A Lista deve ter quantos valores?: '))
minimo = int(input('Menor valor da faixa: '))
maximo = int(input('Maior valor da faixa: '))
numeros = []
preencher(numeros, qtdNumeros, minimo, maximo)
print(numeros)