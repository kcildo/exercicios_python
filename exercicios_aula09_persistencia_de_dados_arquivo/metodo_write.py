# Criando um arquivo texto
# O programa abaixo pede ao usuário que escolha um nome de
# arquivo e quantidade de linhas que deseja escrever, em seguida
# os seus conteúdos são lidos do teclado e escritos no arquivo.

nomeArquivo = input('Digite o nome do arquivo que deseja criar: ')
quantasLinhas = int(input('Quantas linhas: '))
dados = open(nomeArquivo, 'w', encoding='utf-8')
for i in range(quantasLinhas):
 nova = input('Linha ' + str(i+1) + ': ')
 dados.write(nova + '\n')
dados.close()

