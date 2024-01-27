largura=int(input('Digite a largura da parede em metros: '))
altura=int(input('Digite a altura da parede em metros: '))
area=largura*altura
tinta=area/2
print('A área de sua parede é de {} m² e é preciso {} litros de tinta para pintá-la.'.format(area,tinta))