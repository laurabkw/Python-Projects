from random import randint

numero=randint(0,5)
entrada=int(input('Adivinhe o número de 0 e 5 que estou pensando: '))
if numero ==entrada:
    print('Parabéns, você acertou!')
else:
    print('Errou, tente denovo na próxima vez.')