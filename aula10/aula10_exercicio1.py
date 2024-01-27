ano_nascimento=int(input('Insira aqui o seu ano de nascimento: '))
idade=2022-ano_nascimento

if idade<=9:
    print('Você tem {} anos de idade, sua categoria é MIRIM.'.format(idade))
elif idade <=14:
    print('Você tem {} anos de idade, sua categoria é INFANTIL.'.format(idade))
elif idade<=19:
    print('Você tem {} anos de idade, sua categoria é JUNIOR.'.format(idade))
elif idade<=25:
    print('Você tem {} anos de idade, sua categoria é SÊNIOR.'.format(idade))
else:
    print('Você tem {} anos de idade, sua categoria é MATER.'.format(idade))