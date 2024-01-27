ano_nascimento=int(input('Digite aqui o ano em que você nasceu: '))
idade=2022-ano_nascimento

if idade==18:
    print('Você tem {} anos de idade, ainda pode se alistar ao exército.'.format(idade))
elif idade>18:
    print('Você tem {} anos de idade, já passou da hora de você se alistar.'.format(idade))
else:
    print('Infelizmente você não pode se alistar no exército, não tem idade o bastante.')