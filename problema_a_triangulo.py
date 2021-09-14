entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada [2])
d = int(entrada[3])

if a + b > c and b + c > a and a + c > b:
    print('S')
elif b + c > d and c + d > b and b + d > c:
    print('S')
elif a + c > d and c + d > a and a + d > c:
    print('S')
elif a + b > d and b + d > a and a + d > b:
    print('S')
else:
    print('N')