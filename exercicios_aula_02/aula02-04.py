# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada para maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

#declarando variáveis recebendo valores da entrada padrão
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
media = (nota1 + nota2)/2
#verificando situação do aluno
if media >= 7 and media < 10:
    print('A média do aluno é %2.2f. Está [APROVADO].'%(media)) #imprimindo na saída padrão
elif media < 7:
    print('A média do aluno é %2.2f. Está [REPROVADO].'%(media)) #imprimindo na saída padrão
elif media == 10:
    print('A média do aluno é %2.2f. Está [APROVADO COM DISTINÇÃO].'%(media)) #imprimindo na saída padrão