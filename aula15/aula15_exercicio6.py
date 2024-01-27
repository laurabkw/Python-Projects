#fatorial 5! 5x4x3x2x1=120
numero=int(input('Digite um número para calcular seu fatorial: '))
c=numero
f=1
print('Calculando {}! = '.format(numero), end=' ')

while c>0:
    print('{}'.format(c), end=' ')
    print(' x ' if c>1 else ' = ', end=' ')
    f*=c #f=f*c
    c-=1 #c=c-1
print('{}'.forma(f))