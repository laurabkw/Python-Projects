valor1=int(input('Digite o primeiro valor: '))
valor2=int(input('Digite o segundo valor: '))

if valor1>valor2:
    maior=valor1
    print('O primeiro valor é maior.')
elif valor2>valor1:
    maior=valor2 
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior.')