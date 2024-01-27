distancia=int(input('Qual a distâcia da sua viagem? '))
if distancia<=200:
    print('Pague {} reais pela sua passagem.'.format(distancia*0.50))
else:
    print('Pague {} reais pela passagem.'.format(distancia*0.45))