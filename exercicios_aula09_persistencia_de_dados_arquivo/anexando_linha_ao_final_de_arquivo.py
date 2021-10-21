# Anexando uma Nova Linha ao
# Final de um Arquivo
nome = input('Diga o nome do arquivo que deseja anexar linha ao final: ')
arquivo = open(nome, 'a')
novaLinha = input('Diga a nova linha: ')
arquivo.write(novaLinha + '\n')
arquivo.close()
