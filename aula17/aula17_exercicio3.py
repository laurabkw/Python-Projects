n1=int(input('Primeiro valor: '))
n2=int(input('Segundo valor: '))

opcao=0

while opcao!=5:
    print('''[1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao=int(input('Selecione a opção desejada: '))

    if opcao==1:
        soma=n1+n2
        print('A soma entre {} e {} é {}.'.format(n1,n2,soma))
    elif opcao==2:
        multiplicacao=n1*n2
        print('O produto entre {} e {} é {}.'.format(n1,n2,multiplicacao))
    elif opcao==3:
        if n1>n2:
            maior=n1
        else:
            maior=n2
        print('Entre os valores {} e {}, o {} é o maior'.format(n1,n2,maior))
    elif opcao==4:
        print('Informe novos números: ')
        n1=int(input('Primeiro número:'))
        n2=int(input('Segundo número: '))
    elif opcao==5:
        print('Finalizando o programa...')
    else:
        print('Opção Inválida.')
    print('#'*10)
    
print('Fim.')