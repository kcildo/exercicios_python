# Faça um Programa que peça as quatro notas de 10 alunos, calcule
# e armazene num vetor a média de cada aluno, imprima o número
# de alunos com média maior ou igual a 7.0.
# --------------------------------------------------//----------------------------------------------------------------------

from random import uniform # Importando a função uniform da biblioteca random para gerar números aleatórios do tipo float
# Subprogramas
def preencheMedia(qtdAluno): # Função para preencher um vetor contendo a média de alunos, deixei configurado para 10 alunos
    medias = [] # Declarando vetor vazio para receber as médias
    for indAluno in range(qtdAluno): # Loop para preencher o vetor média com 10 valores
        print('Digite a nota do {}º aluno'.format(indAluno+1))
        notas = []  # Declarando vetor para receber os valores das 4 notas que será digitadas pelo usuário
        media = 0  # Iniciando variável para receber o calculo da média
        # entrada = input('Digite as 4 notas do aluno separado por espaço no final tecle [ENTER]: ').split()
        for indNota in range(4): # Loop para pedir pro usuário digitar 4 notas do aluno
            # entrada = float(input('Digite a {}ª nota: '.format(indNota+1))) # Pedindo ao usuário o valor das notas e guardando na variável entrada
            entrada = uniform(5.0, 10.0) # Para o caso de querer gerar as notas aleatóriamente na faixa de 5.0 a 10.0
            notas.append(round(entrada, 1)) # Incluindo as notas digitas no vetor notas com o método append. O metódo round configura as notas para ter apenas um casa apóis o ponto
            media += notas[indNota]/4 # Calculando a média e guardando na variável media
            print('Notas geradas aleatóriamente!!!') # Imprimindo na saída padrão - usar no caso de gerar as notas aleatóriamente
        medias.append(round(media, 1)) # Armazenando as médias calculadas no for anterior
        print('-'*50) # Imprimindo um separador entre as notas dos alunos na saída padrão
    print('Médias: ',medias) # Imprimindo o vetor contendo as 10 médias calculadas
    return medias # Retornando o vetor medias para o Programa Principal
def contaAluno(medias): # Função para contar quantos alunos atingiram média igual ou maior que 7.0
    totAlunos = 0 # Iniciando variável contadora
    for indMedias in medias: # Loop para pegar os valores de cada índice do vetor medias
        if indMedias >= 7: # condicional para verificar se o valor de cada índice é maior ou igual a 7.0
            totAlunos += 1 # Caso a condição acima seja verdadeira a variável contadora será incrementada com + 1
    if totAlunos == 0: # Caso não tenha média maior ou igual a 7.0 apresentará msg ao usuário
        print('\nQue pena! Ninguém atingiu média maoir ou igual a 7.0') # Imprimindo na saída padrão
        exit() # Finalizando o programa para que não imprima a próx linha
    print('\nMaravilha! {} alunos antigiram média maior ou igual a 7.0.'.format(totAlunos)) # imprimindo na saída padrão a quantidade de médias maior ou igual a 7.0
# Programa Principal
mediasAlunos = preencheMedia(10) # Chamando a função preencherMedia passando como parâmetro o valor 10 que será o número de alunos e armazenando o retorno em uma variável
contaAluno(mediasAlunos) # Chamando a função contaAluno passando como parâmetro o vetor retornado da função preencherMedia