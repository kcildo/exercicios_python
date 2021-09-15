# Faça um programa que leia e valide as seguintes informações:
#
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

# declarando variável recebendo valor da entrada padrão
nome = input('Informe seu nome: ')
# Utilizando loop while para verificar se atende a condição pedida
while len(nome) <= 3:
    # imprimindo na entrada padrão
    print('\nERRO! NOME DEVE POSSUIR MAIS DE 3 CARACTERES.\n')
    # pedindo nova string para atualizar a variável e verificar se atende...
    # ...a condição de parada do while
    nome = input('Informe seu nome: ')

# declarando variável recebendo valor da entrada padrão
idade = int(input('Informe sua idade: '))
while (idade <= 0) or (idade >= 150):
    # imprimindo na entrada padrão
    print('\nERRO! IDADE DEVE SER MAIOR QUE [0] E MENOR QUE [150].')
    # pedindo novo inteiro para atualizar a variável e verificar se atende...
    # ...a condição de parada do while
    idade = int(input('Informe sua idade: '))

# declarando variável recebendo valor da entrada padrão
salario = float(input('Informe salário: '))
while salario <= 0:
    # imprimindo na entrada padrão
    print('\nERRO! SALÁRIO DEVE SER MAIOR QUE [0].')
    # pedindo novo inteiro para atualizar a variável e verificar se atende...
    # ...a condição de parada do while
    salario = float(input('Informe salário: '))

# imprimindo na entrada padrão
print('''\nInforme Seu sexo:
"f" --> Feminino 
"m" --> Masculino''')
# declarando variável recebendo valor da entrada padrão
sexo = input('Informe sexo: ')
while (sexo != 'f') and (sexo != 'm'):
    # imprimindo na entrada padrão
    print('''\nERRO! FAVOR Informar:
"f" --> Feminino 
"m" --> Masculino''')
    # pedindo nova string para atualizar a variável e verificar se atende...
    # ...a condição de parada do while
    sexo = input('Informe sexo: ')

# imprimindo na entrada padrão
print('''\nInforme Seu estado civil:
"s" --> Solteiro(a) 
"c" --> Casado(a)
"v" --> Viúvo(a)
"d" --> Divorciado(a)''')
# declarando variável recebendo lista com as strings...
# ...esperadas para condição de parada do loop
situacao = ['s', 'c', 'v', 'd']
# declarando variável recebendo valor da entrada padrão
estadoCivil = input()
while estadoCivil not in situacao:
    # imprimindo na entrada padrão
    print('''\nERRO! FAVOR INFORMAR:
"s" --> Solteiro(a) 
"c" --> Casado(a)
"v" --> Viúvo(a)
"d" --> Divorciado(a)''')
    # pedindo nova string para atualizar a variável e verificar se atende...
    # ...a condição de parada do while
    estadoCivil = input('Informe Estado Civil: ')