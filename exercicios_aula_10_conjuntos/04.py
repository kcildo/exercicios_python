# Exemplo: Este programa gera e imprime os números
# primos entre 2 e N, escolhido pelo usuário, usando o
# algoritmo chamado de “Crivo de Eratóstenes”.

# Subprogramas
def imprime(num, osPrimos):
	print(f'Primos entre 2 e {num}:')
	for candidato in range(2, num + 1):
		if candidato in osPrimos:
			print(candidato, end=' ')
	print()
	return None

def eratostenes(num):
	resposta = set()  # inicializa resposta
	vazio = set()  # inicializa conjunto vazio
	crivo = set(range(2, num + 1))  # constrói conjunto de 2 a num
	prox = 2
	while crivo != vazio:
		while not (prox in crivo):
			prox += 1
		resposta.add(prox)  # ou resposta = resposta | {prox}
		j = prox
		while j <= num:
			crivo.discard(j)  # ou crivo = crivo – {j}
			j += prox
	return resposta

# Programa Principal - Crivo de Eratostenes
n = int(input('Diga o valor: '))
primos = eratostenes(n)
imprime(n, primos)
