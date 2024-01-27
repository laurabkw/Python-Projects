n = 1
P = 0
while n <= 5:
    numero = int(input('Digite um número: '))
    n = n + 1
    if numero % 2 == 0:
        numero = P
        P = P + 1
print('A quantidade de números pares é {}.'.format(P))