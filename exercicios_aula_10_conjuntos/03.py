# Exemplo: Este programa imprime o número de vogais, e
# dígitos existentes em uma frase.

# Subprograma
def contaVogaisDigitos(frase):
	vogais = {'A', 'Á', 'E', 'É', 'I', 'Í', 'O', 'Ó', 'U', 'Ú',
	          'a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'u', 'ú',}
	digitos = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
	nVogais = 0
	nDigitos = 0
	for letra in frase:
		if letra in vogais:
			nVogais += 1
		elif letra in digitos:
			nDigitos += 1
	print(f'Quantidade de Vogais: {nVogais}')
	print(f'Quantidade de Dígitos: {nDigitos}')
	return None

# Programa Principal
lida = input('Diga a frase: ')
contaVogaisDigitos(lida)
