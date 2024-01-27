reta1=int(input('Digite um valor para a primeira reta: '))
reta2=int(input('Digite um valor para a segunda reta: '))
reta3=int(input('Digite um valor para a terceira reta: '))

if reta1==reta2 and reta2==reta3 and reta1==reta3:
    print('O triângulo tem todos os lados iguais, protanto, é equilátero.')
elif reta1!=reta2 and reta2!=reta3 and reta1!=reta3:
    print('O triângulo possui todos os lados diferente, portanto, é escaleno')
else:
    print('O triângulo possui somente 2 lados iguais, portanto, é isósceles.')