# Lista de listas
mercado = [['pera', 100, 4.9], ['manga', 20, 3.9], ['uva', 30, 5.9], ['caju', 15, 3.5]]
print(mercado)

mercado[1][2] *= 0.5 # manga pela metade do preço
print(mercado)

mercado[3][1] -= 10
print(mercado)  # caju com dez quilos a menos

mercado.remove(['uva', 30, 5.9]) # o produto uva é removido do mercado
print(mercado)

mercado.insert(1, ['kiwi', 200, 1.99]) # o produto kiwi foi inserido
print(mercado)
