pergunta=int(input('## Programa de Numerais ## \n Responda: 1 - Binário, 2 - Octal ou 3 - Hexadecimal '))

numero=int(input('Digite aqui um número de sua escolha: '))

if pergunta ==1:
    print('Você escolheu Binário.')
    print('O número que você escolheu em binário é: {}'.format(bin(numero)))
else:
    if pergunta==2:
        print('Você escolheu Octal')
        print('O número que você escolheu em octal é: {}'.format(oct(numero)))

    if pergunta==3:
        print('Você escolheu Hexadecimal')
        print('O número que você escolheu em hexadecimal é: {}'.format(hex(numero)))
    else:
        print('Fechando o programa...')
        exit()