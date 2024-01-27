pa=0
n=int(input('Informe o primeiro termo da PA: '))
razao=int(input('Informe a razão da PA: '))
fim=n+9*razao
for c in range(n,razao+fim, razao):
    print('A PA é {}.'.format(c))
print('Acabou.')