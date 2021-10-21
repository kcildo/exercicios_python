# O Método readline()
#  lê somente uma linha
# dados = open('teste.txt', 'r')
# linha = dados.readline()
# print(linha, end='')
# dados.close()

#  lê a o texto todo
nomeArquivo = input('Digite o nome do arquivo que deseja visualizar: ') # pede para o usuário entrar com o nome do arquivo a ser lido
dados = open(nomeArquivo, 'r')
linha = dados.readline()
while linha != '':
 print(linha, end='')
 linha = dados.readline()
dados.close()