# Faça um programa que leia um nome de usuário e a sua senha e não
# aceite a senha igual ao nome do usuário, mostrando uma mensagem
# de erro e voltando a pedir as informações.

# declarando variáveis recebendo valor de entrada padrão
nome = input('Digite o nome de usuário: ')
senha = input('Digite a senha: ')

# loop com condição de parada de nome != senha
while nome == senha:
    # imprimindo na saída padrão
    print('\nERRO! NOME NÃO PODE SER IGUAL A SENHA.\n')

    # Solicitando dados novamente para atualizar...
    # ...valores em variáveis e não gerar loop infinito
    nome = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')