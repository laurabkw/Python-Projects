print('## Programa de empréstimos ## \n Responda: 0 - Não e 1- Sim')

nome_negativado=int(input('Possui nome negativado? '))
if nome_negativado ==1:
    print('Não pode realizar o empréstimo.')
else:
    print('Concede empréstimo.')

carteira_assinada=int(input('Possui carteira assinada? '))
if carteira_assinada==0:
    print('Não pode realizar o empréstimo.')
else:
    print('Concede empréstimo.')

possuiCasa_Propria=int(input('Possui casa própria? '))
if possuiCasa_Propria==0:
    print('Não pode realizar o empréstimo.')
else:
    print('Concede empréstimo.')