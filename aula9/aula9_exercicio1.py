valor_casa=int(input('Digite o valor da casa comprada: '))
salario=int(input('Digite aqui o seu salário: '))
anos=int(input('Em quantos anos você pagará a casa? '))
salario_prestacao=salario*0.30
valor_prestacao=valor_casa/(anos/12)

if valor_prestacao<=salario_prestacao:
    print('Você pode pagar pela casa.')
else:
    print('Você não pode pagar pela casa.')