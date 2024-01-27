velocidade=int(input('Digite aqui a velocidade que o seu carro esta se movendo: '))

if velocidade>=80:
    print('Infelizmente você ultrapassou o limite de velocidade, pague {} reais de multa.'.format(velocidade*7))
else:
    print('Você está dentro do limite de velocidade, pode continuar com sua viajem.')
