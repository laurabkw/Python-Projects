from html.entities import codepoint2name
from math import sqrt

x1=float(input('Digite a coordenada x do Ponto 1: '))
y1=float(input('Digite a coordenada y do Ponto 1: '))

x2=float(input('Digite a coordenada x do Ponto 2: '))
y2=float(input('Digite a coordenada y do Ponto 2: '))

x3=float(input('Digite a coordenada x do Ponto 3: '))
y3=float(input('Digite a coordenada y do Ponto 3: '))

l1=sqrt(pow(x2-x1,2)+pow(y2-y1,2))
l2=sqrt(pow(x3-x1,2)+pow(y3-y1,2))
l3=sqrt(pow(x3-x2,2)+pow(y3-y2,2))

cond1=True
cond2=True
cond3=True

if l1==0 or l2==0 or l3==0:
    cond1=False

if l1>(l2+l3) or l2>(l1+l3) or l3>(l2+l1):
    cond2=False

if l1<=abs(l2-l3) or l2<=abs(l1-l3) or l3<=abs(l1-l2):
    cond3=False

triangulo=True

if cond1==False or cond2==False or cond3==False:
    triangulo=False
    print('Nenhum triângulo formado.')

    if cond1==False:
        print('Pelo menos um dos lados é igual a zero.')

    if cond2==False:
        print('Pelo menos um dos lados é maior que a soma dos outros dois lados.')

    if cond3==False:
        print('Pelo menos um dos lados é menor ou igual ao módulo da diferença.')

elif l1==l2==l3:
    print('Triângulo equilátero.')

elif l1!=l2!=l3:
    print('Triângulo escaleno.')
else:
    print('Triângulo isósceles')

if triangulo:
    print('Medida do lado 1 {}, lado 2 {} e lado 3 {}'.format(l1, l2, l3))