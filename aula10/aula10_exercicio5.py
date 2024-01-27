numero_camisas=int(input('Digite aqui o número de camisetas que você comprou: '))
preco=int(input('Digite aqui o preço unitário das camisetas: '))

if numero_camisas==5:
    desconto1=preco-preco*0.03
    print('Você comprou {} camisetas, o preço delas fica {}.'.format(numero_camisas,desconto1))
elif numero_camisas>5 and numero_camisas<=10:
    desconto2=preco-preco*0.05
    print('Você comprou {} camisetas, o preço delas fica {}.'.format(numero_camisas,desconto2))
else:
    desconto3=preco-preco*0.07
    print('Você comprou {} camisetas, o preço delas fica {}.'.format(numero_camisas,desconto3))