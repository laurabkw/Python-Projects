maior=0
menor=1000
for c in range(0,6):
    peso=float(input('Informe o peso: '))
    if peso>maior:
        maior=peso
    elif peso<menor:
        menor=peso
print('{} foi o maior peso digitado e {} foi o menor peso digitado.'.format(maior,menor))