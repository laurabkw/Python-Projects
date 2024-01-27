nota1=int(input('Digite aqui a primeira nota: '))
nota2=int(input('Digite aqui a segunda nota: '))
media=(nota1+nota2)/2

if media>=7:
    print('Parabéns, você foi aprovado com média {}.'.format(media))
elif media>=5 and media<=6.9:
    print('Você deverá ficar de recuperação pela sua média {}.'.format(media))
else:
    print('Infelizmente você foi reprovado.')