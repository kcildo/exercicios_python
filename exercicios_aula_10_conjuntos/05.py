# Este subprograma imprime o conjunto de características
# comuns a todos os indivíduos pertencentes a um
# subconjunto de uma determinada população. Cada
# indivíduo da população está associado a um identificador
# (0..MaxPop-1) e possui um conjunto de características.

# Subprograma
def perfilComum(habitantes, caracteristicas, grupo):
	comuns = caracteristicas
	for ident in range(len(habitantes)):
		if ident in grupo:
			comuns = comuns & habitantes[ident] # ou intersection
	print('As características em comum são:')
	for c in caracteristicas:
		if c in comuns:
			print(c, end=' ')
	print()
	return None

# Programa Principal
caracteristicas = {'esporte', 'tv', 'cinema', 'livro', 'jornal', 'teatro', 'musica'}
alunos = [{'tv', 'cinema', 'livro'}, {'cinema', 'musica'}, {'cinema', 'tv', 'teatro'}]
perfilComum(alunos, caracteristicas, {2, 0})
