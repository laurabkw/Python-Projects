reta1=int(input('Digite um valor para a primeira reta: '))
reta2=int(input('Digite um valor para a segunda reta: '))
reta3=int(input('Digite um valor para a terceira reta: '))

if reta1<reta2+reta3 and reta2<reta1+reta3 and reta3<reta1+reta2:
    print('As retas acima PODEM formar um triângulo.')
else:
    print('As retas acima NÃO PODEM formar um triângulo.')