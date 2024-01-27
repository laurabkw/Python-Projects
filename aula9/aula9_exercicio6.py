pergunta=int(input('## Programa de Cálculo de Grandezas Elétricas ## \n Qual grandeza deseja calcular? Responda: 1 - Tensão (em Volts), 2 - Resistência (em Ohm) ou 3 - Corrente (em Ampére) '))

if pergunta==1:
    resistencia=input('Informe o valor da Resistência: ')
    corrente=input('Informe o valor da Corrente: ')
    tensao=resistencia*corrente
    print('Você escolheu calcular a Tensão, seu valor é de {} voltz.'.format(tensao))
    
elif pergunta==2:
    tensao=input('Informe o valor da Tensão: ')
    corrente=input('Informe o valor da Corrente: ')
    resistencia=tensao/corrente
    print('Você escolheu calcular a Resistência, seu valor é de {} ohms.'.format(resistencia))
    
else:
    tensao=input('Informe o valor da Tensão: ')
    resistencia=input('Informe o valor da Resistencia: ')
    corrente=tensao/resistencia
    print('Você escolheu calcular a Resistência, seu valor é de {} ampéres.'.format(corrente))
    