salario_pergunta=int(input('Quanto é o seu salário? '))

if salario_pergunta>=1250:
    print('Você acabou de receber um aumento! Agora você recebe {} reais.'.format(salario_pergunta*0.10))
else:
    print('Você acabou de receber um aumento! Agora você recebe {} reais.'.format(salario_pergunta*0.15))