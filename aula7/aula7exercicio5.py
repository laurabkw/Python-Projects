entrada=int(input('## Programa de Cálculos ## \n Responda: 1 - Média Ponderada, 2 - Quadrado da Soma de Dois Números ou 3 - Cubo do Menor Número '))

numero1=int(input('Escolha um valor para o primeiro número: '))
numero2=int(input('Escolha um valor para o segundo número: '))

if entrada ==1:
    print('Você escolheu média ponderada.')
    media=((numero1*2)+(numero2*3))/2
    print('O valor de sua média é igual á: ',media)
else:
    if entrada==2:
        print('Você escolheu o quadrado da soma dos números.')
        quadrado=(numero1+numero2)**2
        print('O quadrado da soma dos números escolhidos é: ',quadrado)

    if entrada==3:
        print('Você escolheu o cubo do menor número')
        if numero1>numero2:
            cubo=(numero1**3)
            print('O número {} é MAIOR que o número {}.'.format(numero1,numero2))
        else:
            cubo=(numero2**3)
            print('O número {} é MENOR que o número {}.'.format(numero1,numero2))
    else:
        print('Fechando o programa...')
        exit()