from random import randrange

n=int(input('Informe o valor de N: '))

if n>0:
    lista1=[randrange(1,11) for i in range(n)]
    lista2=[randrange(1,11) for i in range(n)]

    lista3=[]

    for i in range(n):
        lista3.append(lista1[i]+lista2[i])

    print('Lista 1 = {}'.format(lista1))
    print('Lista 2 = {}'.format(lista2))
    print('Lista 3 = {}'.format(lista3))
else:
    print('Erro: N não deve ser maior que 0')