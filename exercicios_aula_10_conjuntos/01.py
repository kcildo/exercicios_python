# O programa abaixo faz a leitura de cinco nomes e cria um conjunto com
# até cinco nomes distintos digitados pelo usuário. A impressão do
# conteúdo do conjunto ocorre a cada tentativa de inclusão de nome.
# Criando um Conjunto de Nomes via Teclado

escolhidos = set()
for i in range(5):
	nome = input('Digite nome: ')
	escolhidos.add(nome)
	print(escolhidos)

# Criando um Conjunto de Nomes Diretamente
escolhidos = {'Maria', 'Ana', 'Giovanna', 'Leandro', 'Dante'}
print(escolhidos)
