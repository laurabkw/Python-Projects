from datetime import date
atual=date.today().year
nascimento=int(input('Ano de nascimento: '))
idade=atual-nascimento
print('O atleta tem {} anos de idade.'.format(idade))

if idade<=9:
    print('Categoria: MIRIM')
elif idade <=14:
    print('Categoria: INFANTIL')
elif idade<=19:
    print('Categoria: JUNIOR')
elif idade<=25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')