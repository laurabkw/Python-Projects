print('Código de cargo: n\1 = Enfermeiro n\2 =  Nutricionista n\3 = Médico(a)')

qtde_nutri=0
total_sal_nutri=0

while True:
    cargo=int(input('Informe um código de cargo: '))
    if cargo>=1 and cargo<=3:
        salario=float(input('Salário R$: '))
        if cargo==2:
            qtde_nutri+=1
            total_sal_nutri+=salario
        resp=input('Deseja continuar [S/N]: ')
        if resp.upper()=='N':
            break
    else:
        print('Código Inválido.')

if qtde_nutri>0:
    media=total_sal_nutri/qtde_nutri
    print('Média salarial  das nutricionistas: R$ {}'.format(media))