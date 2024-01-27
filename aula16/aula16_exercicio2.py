nome=input('Informe o nome do medicamento que você deseja comprar: ')
preco=float(input('Insira aqui o preço do medicamento: '))
soma=0
media=0

nome_medicamento_barato=nome
preco_medicamento_barato=preco

for c in range (1,5):
    nome=input('Informe o nome do medicamento que você deseja comprar: ')
    preco=float(input('Insira aqui o preço do medicamento: '))
    soma+=preco

    if preco<preco_medicamento_barato:
        preco_medicamento_barato=preco
        nome_medicamento_barato=nome
media=soma/5
print('{} é o medicamento mais barato e custa R$ {}\nMédia dos valores: R${}.'.format(nome_medicamento_barato, preco_medicamento_barato, media))