idade=int(input('Insira a sua idade: '))

if (idade >= 0 and idade <= 12):
    print('Você recebe 15 por cento de desconto.')
if (idade >= 13 and idade <= 18):
    print('Você recebe 12 por cento de desconto.')
if (idade >= 19 and idade <= 21):
    print('Você recebe 5 por cento de desconto.')
if (idade >= 22 and idade <= 24):
    print('Você recebe 3 por cento de desconto.')
if (idade >= 25):
    print('Você não recebe desconto.')