def area(largura, comprimento):
    area_terreno=largura*comprimento
    return area_terreno

largura=int(input('Digite a largura do terreno: '))
comprimento=int(input('Digite o comprimento do terreno: '))
print('A área do terreno é de {} metros quadrados.'.format(area(largura,comprimento)))