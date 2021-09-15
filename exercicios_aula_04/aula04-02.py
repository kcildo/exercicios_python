# Faça um Programa que leia um vetor de 10 números reais e
# mostre-os na ordem inversa.
# ------------------------------------------------------------//-----------------------------------------------------

print('''Digite 10 números inteiros para compor um vetor,
em seguida o mesmo será mostrado na ordem inversa.
''')

vetor = []  # Iniciando variável para armazenar vetor
vetorReverso = []

while len(vetor) < 10:  # Lopping para ler e preencher o vetor com números inteiros
    entrada = int(input('Digite o {}º número: '.format(len(vetor) + 1)))
    vetor.append(entrada)  # Adicionando números no vetor
print('\nSeu vetor digitado foi: ', vetor)  # Imprimindo na saída padrão

cont = len(vetor)  # Iniciando a variável contadora atribuindo o tamanho total do vetor preenchido acima
while cont > 0:  # Lopping para pecorrer o vetor inversamente e armazenar os valores em um novo vetor
    cont -= 1
    vetorReverso.append(vetor[cont])  # Adicionando de maneira inversa os valores do vetor original em um novo vetor
print('\nO vetor inveso é: ', vetorReverso)  # Imprimindo na saída padrão


