# Faça um Programa que leia três números e
# mostre o maior e o menor deles.
Pontos a serem tomadas:
cont = maior = menor =  0 #declarando variáveis
print('Digite 3 números. Após cada número tecle [ENTER]: ')
while cont < 3:
    entrada = float(input('Digite o %dº número: '%(cont+1))) #recebendo números reais
   #Verificando maior e menor entre números digitados
    cont += 1
    if cont == 1:
        maior = menor = entrada
    elif entrada > maior:
        maior = entrada
    elif entrada < menor:
        menor = entrada
#Imprimindo na saída padrão
print('''O maior valor digitado foi: %4.2f. 
O menor valor digitado foi: %4.2f''' %(maior, menor))