# Processamento Recursivo de Listas (Lisp-Like)
def car(dados):
    return dados[0]
def cdr(dados):
    return dados[1:len(dados)]
def cons(item, dados):
    return [item]+dados
def soma(dados):
    if dados == []:
        return 0
    else:
        return car(dados) + soma(cdr(dados))
lista = [0,1,2,3,4,5,6,7,8,9]
print(f'lista original: {lista}')
print(f'Fatiamento da lista a partir do segundo elemento: {lista[1:]}')
print(f'Soma de todos os elementos da lista {soma(lista)}')