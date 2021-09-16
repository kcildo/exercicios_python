# Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser
# compostos pelos elementos intercalados dos dois outros vetores.
from random import randint # Importando a função randint da biblioteca random para gerar números aleatórios
# Subprogramas
def preencheVetor(a, b): # Função para preencher vetor com números aleatórios onde o número de ínicio e fim é passado pelo usuário
    vetor = []
    for i in range(10): # Loop de 0 a 10 para preencher o vetor com 10 elementos
        elementos = randint(a, b) # Variável recebendo um número aleatório dentro do intervalo passado
        vetor.append(elementos) # Vetor recebendo cada elemento no final atravéz da função append
    return vetor # Retornando o vetor preenchido para o programa principal
def misturaVetores(vetor1, vetor2): # Função para receber dois vetores e gerar um terceiro vetor com os elementos intercalados do vetor1 e vetor2
    vetorFilho = []
    for i in range(10): # loop para preencher o vetor com os elementos do vetor1 e vetor2
        vetorFilho.append(vetor1[i]) # Incluindo os elementos do vetor1 no final do novo vetor
        vetorFilho.append(vetor2[i]) # Logo após um elemento do vetor1 ser incluso será incluso um elemento do vetor2
    return vetorFilho # Retornando o novo vetor para o programa principal
# Programa Principal
print('''Digite uma faixa númerica (ínicio e fim). EXEMPLO:
Início = 11
Fim = 20
Para ficar interessante digite duas faixas diferentes!!!''')
#Chamando a função preencheVetor passando como parâmetro o número de início e fim do intervalo digitado pelo usuário
pai = preencheVetor(float(input('\nIntervalo1 - Início = ')), float(input('Intervalo1 - Fim = ')))
mae = preencheVetor(float(input('\nIntervalo2 - Início = ')), float(input('Intervalo2 - Fim = ')))
#Chamando a função misturaVetores passando como parâmetro os vetores retornados pela função preencheVetor
filho = misturaVetores(pai, mae)
#Imprimindo na saída padrão
print('''
Vetor pai: {}
Vetor mãe: {} 
Vetor filho: {} '''.format(pai, mae, filho))
