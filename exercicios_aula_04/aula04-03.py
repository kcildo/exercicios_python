# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas
# consoantes foram lidas. Imprima as consoantes.

entradas = [] # Iniciando variável recebendo uma lista vazia
consoantes = 0 # Iniciando variável contadora
print('''Digite 10 caracteres para formar um vetor de caracteres.
''')
while len(entradas) < 10: # Iniciando um lopping para preencher o vetor
    entradas.append(input('Digite o {}º caracter: '.format(len(entradas)+1)))

print('\nAs consoantes digitadas foram: ', end='')
for entrada in entradas: # lopping para pecorrer o vetor e comparar os caracteres digitados
    if entrada not in 'aeiouAEIOU': # Condicional para comparar os caracteres com vogais
        consoantes += 1 # Se o carcter não for vogal a variável contadora será incrementada com + 1
        print(entrada, end=' ') # Imprimindo na saída padrão na mesma linha que o print anterior

# Imprimindo na saída padrão o total de consoantes lidas
print('\n\nTotalizando {} consoantes.'.format(consoantes))

