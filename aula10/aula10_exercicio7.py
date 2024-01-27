cargo=int(input('Digite aqui o seu cargo: 1 - Programador de Sistemas, 2 - Analista de Sistemas ou 3 - Analista de Banco de Dados. '))
salario=float(input('Digite aqui o seu salário: '))

if cargo==1:
    print('Seu cargo é de Programador de Sistemas.')
    programador_s=salario*0.30
    print('Você recebeu um aumento, seu salário antes era {} reais agora é {} reais.'.format(salario,programador_s))
elif cargo==2:
    print('Seu cargo é de Analista de Sistemas.')
    analista_s=salario*0.20
    print('Você recebeu um aumento, seu salário antes era {} reais agora é {} reais.'.format(salario,analista_s))
elif cargo==3:
    print('Seu cargo é de Analista de Banco de Dados.')
    abd=salario*0.15
    print('Você recebeu um aumento, seu salário antes era {} reais agora é {} reais.'.format(salario,abd))
else:
    print('Cargo Inválido')