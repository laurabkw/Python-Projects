while True:
    n=int(input('Digite aqui um número para ver sua tabuada: '))
    if n<0:
        break
    for c in range(1,11):
        print('{} x {} = {}'.format(n,n,n*c))
print('Programa tabuada encerrado.')