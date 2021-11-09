#  Copiando um arquivo texto
# Subprogramas
def mostra(nome):
 infos = open(nome, 'r', encoding='utf-8')
 for linha in infos:
    print(linha.strip())
 infos.close()
 print()
 return None
def copiar(nomeOrigem, nomeDestino):
 orig = open(nomeOrigem,'r', encoding='utf-8')
 dest = open(nomeDestino, 'w', encoding='utf-8')
 for linha in orig:
    dest.write(linha)
 orig.close()
 dest.close()
 return None
# Programa Principal
nomes = input('Escreva os nomes dos arquivos, original e destino: ').split()
mostra(nomes[0])
copiar(nomes[0], nomes[1])
mostra(nomes[1])