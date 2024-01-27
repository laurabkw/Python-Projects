from aula28_exercicio0a import *

escolha=int(input('Escolha uma das opções: \n1.Soma \n2.Subtração \n3.Divisão \n4.Multiplicação \n5.Todas as operações '))

numero1=int(input('Digite o primero número: '))
numero2=int(input('Digite o segundo número: '))

if escolha<0 or escolha>5:
    print('Opção Invalida.')
elif escolha==1:
    s=soma(numero1,numero2)
    print('A soma entre {} e {} é igual a {}.'.format(numero1,numero2,s))
elif escolha==2:
    sb=subtracao(numero1,numero2)
    print('A subtração entre {} e {} é igual a {}.'.format(numero1,numero2,sb))
elif escolha==3:
    d=divisao(numero1,numero2)
    print('A divisão entre {} e {} é igual a {}.'.format(numero1,numero2,d))
elif escolha==4:
    m=multiplicacao(numero1,numero2)
    print('A multiplicação entre {} e {} é igual a {}.'.format(numero1,numero2,m))
elif escolha==5:
    c=calculadora(numero1,numero2)
    print(f'Soma={c[0]}, Subtração={c[1]}, Divisão={c[2]:.2f}, Multiplicação={c[3]}')