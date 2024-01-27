soma=0
for c in range(0,7):
    n=int(input('Informe o número: '))
    if n%2==0:
        soma+=n
print('A soma dos números pares é {}.'.format(soma))