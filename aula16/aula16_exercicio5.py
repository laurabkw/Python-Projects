idade=int(input('Idade: '))

mais_novo=idade
mais_velho=idade

while True:
    idade=int(input('Idade: '))
    if idade<0:
        break

    if idade<mais_novo:
        mais_novo=idade
    elif idade>mais_velho:
        mais_velho=idade

media=(mais_novo+mais_velho)/2

print('Menor idade: {}\nMaior idade: {}\nMedia das duas idades: {}'.format(mais_novo,mais_velho,media))