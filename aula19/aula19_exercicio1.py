numero=int(input('Digite um número: '))
sequencia=0
n1=0
n2=1
print('{}, {}'.format(n1,n2),end=',')

for c in range (numero):
    sequencia=n1+n2
    print('{}'.format(sequencia),end=',')
    n1=n2
    n2=sequencia