total=totmil=menor=cont=0
barato=' '
while True:
    produto=input('Nome do produto: ')
    preco=float(input('Preço R$: '))
    cont+=1
    total+=preco
    if preco>1000:
        totmil+=1
    if cont==1 or preco<menor:
        menor=preco
        barato=produto
    resposta=' '
    while resposta not in 'SN':
        resposta=input('Quer continuar [S/N]? ').strip().upper()
    if resposta=='N':
        break
print('O total das compras  for de R$ {}.'.format(total))
print('Temos {} produtos custando mais de R$ 1000,00.'.format(totmil))
print('O produto mais barato foi {} que custa R$ {}.'.format(produto,menor))