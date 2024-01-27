ano=int(input('Digite aqui um ano qualquer para saber se ele é bissexto: '))
if ano%4 ==0:
    print('O ano {} não é bissexto.'.format(ano))
else:
    print('O ano {} escolheu é bissexto.'.format(ano))