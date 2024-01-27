soma=0
n=0
numero=0

while numero!=999:
    n+=1
    soma+=numero
    numero=int(input('Digite um número: '))
print('A soma de todos os {} números que foram digitados é igual a {}.'.format(n-1,soma))