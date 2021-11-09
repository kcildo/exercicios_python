# Operadores para Conjuntos

# Exemplo: Utilizando os operadores que sobre conjuntos,
# declare variáveis do tipo conjunto para representarem: um
# ano, as férias de fim de ano, as férias de meio de ano, todas
# as férias e o período letivo de um ano

ano = {'jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'}
feriasFimAno = {'jan', 'fev', 'dez'}
feriasMeioAno = {'jul'}
ferias = feriasFimAno.union(feriasMeioAno)
print(f'Período de férias {ferias}')
periodoLetivo = ano.difference(ferias)
print(f'Período letivo {periodoLetivo}')