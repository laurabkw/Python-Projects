from random import randrange

n=int(input('Digite um número, deve ser maior que 1: '))
lista=[randrange(1,11) for i in range(n)]
media=1

for n in lista:
    media*=n

media=media**1/n

print('A média dos elementos da lista é {}'.format(media))