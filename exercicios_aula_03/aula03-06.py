# Faça um programa que converta da notação de 24 horas para a
# notação de 12 horas. Por exemplo, o programa deve converter 14:25
# em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo
# menos duas funções:
#
# - uma para fazer a conversão;
#
# - uma para a saída.
#
# Registre a informação A.M./P.M. como um valor ‘A’ para A.M.
# e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um
# parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que
# permita que o usuário repita esse cálculo para novos valores de
# entrada todas as vezes que desejar.
#
# Não esqueça de trabalhar a interface.
# ------------------------------------------------------------//---------------------------------------------------------------------------------

# Subprogramas
def convertHora(hora):
    novaHora = int(hora[0]) # Convertendo o valor do primeiro indice da lista hora para inteiro onde poderei fazer as comparações com números
    if (novaHora >= 1) and (novaHora <= 11):
        hora.append('A.M')
        return escreveHora(hora) # Chamando a função escreveHora passando a lista com a hora modificada como parâmetro
    elif novaHora == 12:
        hora.append('P.M')
        return escreveHora(hora) # Chamando a função escreveHora passando a lista com a hora modificada como parâmetro
    elif novaHora == 00:
        novaHora += 12
        hora[0] = novaHora
        hora.append('A.M')
        return escreveHora(hora) # Chamando a função escreveHora passando a lista com a hora modificada como parâmetro
    elif (novaHora >= 13) and (novaHora <= 23):
        novaHora -= 12
        hora[0] = novaHora
        hora.append('P.M')
        return escreveHora(hora) # Chamando a função escreveHora passando a lista com a hora modificada como parâmetro
def escreveHora(hora):
    print()
    print(*hora) # Imprimindo na saída padrão sem o formato da lista
    return None
# Programa Principal
print('''Conversão de hora do formado 24hs para o formato 12h
Exemplo: 23:50 -> 11:50P
Quando solicitado digite dois inteiros representando
hora e minutos do formato 24hs. Ex: [13 30] e tecle [ENTER]''')
resp = 'S'
while resp in 'Ss': #looping para permitir rodar a quantidade de vez que quiser
    entrada = input('\nDigite dois inteiros separados por espaço: ').split() #iniciando variável recebendo valores da entrada padrão transformando a mesma em uma lista
    convertHora(entrada) # Chamando a função convertHora passando uma lista com os valores digitados
    resp = str(input('\nDeseja continuar? [S/N] ')).upper().strip()[0] # Atualizando o valor da variável resp para verificar a condição de parada do loop
