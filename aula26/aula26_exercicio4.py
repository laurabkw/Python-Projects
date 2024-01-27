def sorteia():
    from random import randint
    numeros=randint(0,900)
    return numeros

def somapar(numeros):
    soma=0
    for n in range(numeros):
        if n%2==0:
            soma=soma+n
    return soma

print('A soma dos números sorteados é {}.'.format(somapar(sorteia())))