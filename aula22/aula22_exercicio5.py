from math import sqrt

lista=[9,3,5,7,2,1]
menor=min(lista)
maior=max(lista)
media_geo=sqrt(menor*maior)

print('Lista: {}'.format(lista))
print('Média geométrica entre {} e {} é igual a: {}'.format(menor,maior,media_geo))