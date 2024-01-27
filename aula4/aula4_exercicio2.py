from cmath import sqrt


x1=float(input('Digite um valor para X1:'))
y1=float(input('Digite um valor para Y1: '))
x2=float(input('Digite um valor para X2:'))
y2=float(input('Digite um valor para Y2: '))
d1=float(x2-x1)**2
d2=float(y2-y1)**2
d3=float(d1+d2)
d5=(sqrt(d3))
print('O resultado do seu plano cartesiano é: ',d5)