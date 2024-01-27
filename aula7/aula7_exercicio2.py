numero1=int(input('Digite aqui um valor para o primeiro número: '))
numero2=int(input('Digite aqui um valor para o segundo número: '))
numero3=int(input('Digite aqui um valor para o terceiro número: '))

menor = numero1
if numero2<numero1 and numero2<numero3:
    menor=numero2
if numero3<numero1 and numero3<numero2:
    menor=numero3

maior = numero1 
if numero2>numero1 and numero2>numero3:
    maior = numero2 
if numero3>numero1 and numero3>numero2:
    maior = numero3

print('O MENOR valor digitado foi {}.'.format(menor))
print('O MAIOR valor digitado foi {}.'.format(maior))