n = int(input('Digite um número inteiro: '))
quantDiv = 0
print('Os números primos de 1 a {} são: '.format(n))
for i in range(1, n+1):
    for c in range(2, i):
        if i % c == 0:
            break
    else:
        print(i, end=' ')
        quantDiv += 1
print(f'.Foram realizadas {quantDiv} divisões.')