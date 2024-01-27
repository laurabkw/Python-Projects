n=int(input('Digite um número ímpar, maior que 1: '))

if n<=1 or n%2==0:
    print('Número informado não atende aos critérios definidos.')
else:
    l=[]
    for x in range(n):
        num=int(input('Digite um número maior ou igual a zero: '))
        l.append(num)

centro=int(len(l)/2)
elemento_centro=1[centro]
fatorial=1

for n in range(2, elemento_centro+1):
    fatorial+=n
print('Lista: {}'.format(l))
print('O elemento dos centro da lista é {} e seu fatorial é igual a {}'.format(elemento_centro,fatorial))