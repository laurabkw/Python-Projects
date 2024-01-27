numero=(int(input('Digite o primeiro valor: ')),
int(input('Digite o segundo valor: ')),
int(input('Digite o terceiro valor: ')),
int(input('Digite o quarto valor: ')))

print('Os números digitados foram: {}'.format(numero))

#letra a
print('O número 9 apareceu {} vezes.'.format(numero.count(9)))

#letra b
if 3 in numero:
    print('O número 3 apareceu na posição {}'.format(numero.index(3)+1))
else:
    print('O número 3 não foi digitado')

#letra c
for n in numero:
    if n %2==0:
        print('Os números pares digitados foram: '.format(n, end=' '))