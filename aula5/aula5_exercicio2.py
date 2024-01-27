from math import hypot
cateto1=float(input('Digite o comprimento do cateto oposto: '))
cateto2=float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa=hypot(cateto1, cateto2)
print('A hipotenusa é {} '.format(hipotenusa))