# Faça um Programa que leia 20 números inteiros e armazene-os num
# vetor. Armazene os números pares no vetor PAR e os números
# IMPARES no vetor impar. Imprima os três vetores.
# ------------------------------------------------------------//-----------------------------------------------------

# Subprogramas
# Definindo uma função recebendo o vetor original como parâmetro para gerar um novo vetor só com números pares
def par(vetor):
    vetorPar = []
    for par in vetor: # Loop para pecorrer o vetor original passado por parâmetro
        if par%2==0: # Condicional para verificar se o elemento do vetor é par
            vetorPar.append(par) # Caso True preenche o vetorPar só com números pares
    return vetorPar # Retornando o vetorPar para o programa principal

# Função análoga a primeira porém dessa vez vamos considerar apenas os números ímpares.
def impar(vetor):
    vetorImpar = []
    for impar in vetor:
        if impar%2!=0:
            vetorImpar.append(impar)
    return vetorImpar

# Programa principal
vetor = [] # Declarando variável recebendo um vetor vazio
while len(vetor) < 20: # Looping para preencher o vetor
    # recebendo números inteiros da entrada padrão
    entrada = int(input('Digite o {}º número: '.format(len(vetor)+1)))
    vetor.append(entrada) # Preenchendo o vetor

# Imprimindo na saída padrão
print('\nO vetor digitado foi: \n{}'.format(vetor))
print('\nO vetor formado só de números pares são: \n{}'.format(par(vetor)))
print('\nO vetor formado só de números ímpares são: \n{}'.format(impar(vetor)))

