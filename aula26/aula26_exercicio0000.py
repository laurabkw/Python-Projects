def calcularMedia(lista):
    soma=0
    for valor in lista:
        soma+=valor
    return float(soma/len(lista))

def calculoDesvioPadrao(lista):
    n=len(lista)
    m=calcularMedia(lista)
    soma=0
    from math import pow, sqrt # pow (potenciação)
    for valor in lista:
        soma+=pow(valor-m,2)
    return sqrt((1/(n-1))*soma)

lista=[3,6,2,9,10,45,36,42,100]

print(calculoDesvioPadrao(lista))