km=int(input('Quantos quilômetros você andou com o carro? '))
dias=int(input('Por quantos dias você alugou o carro? '))
preco_km=km*0.15
preco_dias=dias*60
valor_final=preco_km+preco_dias
print('Você alugou o carro por {} dias e andou {} quilômetros nele, você deverá pagar {} reais pelo uso.'.format(dias,km,valor_final))