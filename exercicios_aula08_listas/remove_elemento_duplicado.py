# Crie uma lista com 100 números aleatórios no intervalo 0 a
# 40. Remova da lista todos os valores duplicados e mostre
# seu conteúdo.
def preencher(listaElems, qtd, min, max):
    from random import randint
    for item in range(qtd):
        listaElems.append(randint(min,max))
    return None
def removerDuplicatas(elems):
    indice = 0
    while indice<len(elems):
        if elems.count(elems[indice])==1:
            indice += 1
        else:
            elems.remove(elems[indice])
    return None
# Programa Principal
numeros = []
preencher(numeros, 100, 0, 40)
print(numeros)
removerDuplicatas(numeros)
print(numeros)
