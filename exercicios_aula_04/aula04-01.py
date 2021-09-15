# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
# ------------------------------------------------------------//-----------------------------------------------------

vetor = []
print('Digite 5 números inteiros para compor um vetor.\n')
while len(vetor) < 5:
    entrada = int(input('Digite o {}º número: '.format(len(vetor)+1)))
    vetor.append(entrada)
print('\nSeu vetor é formato pelos números: {}'.format(vetor))
