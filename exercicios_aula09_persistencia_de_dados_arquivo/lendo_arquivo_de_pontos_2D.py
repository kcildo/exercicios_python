# O programa abaixo faz a leitura de um arquivo, chamado “pontos.txt”, com
# pontos bidimensionais (2D), com coordenadas (x,y). Calcula e escreve o
# centroide de todos os pontos lidos.
# Subprogramas
def centroide(nome):
 arquivo = open(nome, 'r')
 qtdPts = 0
 somaX = 0
 somaY = 0
 for coordenada in arquivo:
  partes = coordenada.split()
  somaX += float(partes[0])
  somaY += float(partes[1])
  qtdPts+=1
 arquivo.close()
 if qtdPts == 0:
  print(arquivo.name, '- vazio!!!')
 else:
  print(f'Ponto calculado: ({somaX / qtdPts:.2f}) ({somaY/qtdPts:.2f}).')
 return None
# Programa Principal – Calcula e escreve o centroide de pontos.
centroide('pontos.txt')