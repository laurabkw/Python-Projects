pagamento=float(input('Escolha sua forma de pagamento: 1 - À vista/Dinheiro, 2 - À vista no cartão, 3 - 2x no cartão. '))
preco=float(input('Digite aqui o valor do produto que você comprou: '))

if pagamento==1:
    print('Você escolheu pagamento à vista.')
    vista_dinheiro=preco-preco*0.10
    print('O preço original era {}, agora o preço é {}.'.format(preco, vista_dinheiro))
elif pagamento==2:
    print('Você escolheu pagamento à vista no cartão.')
    vista_cartao=preco-preco*0.05
    print('O preço original era {}, agora o preço é {}.'.format(preco, vista_cartao))
else:
    print('Você escolheu pagamento 2x no cartão.')
    cartao2=preco
    print('O preço original era {}, agora o preço é {}.'.format(preco,cartao2))