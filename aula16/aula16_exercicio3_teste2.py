erros=0
while erros<3:
    senha=int(input('Senha: '))
    if senha==123456:
        print('Olá, Bem Vindo a sua conta.')
        break
    else:
        erros+=1
    if erros<3:
        print('Senha incorreta. Você ainda tem {} tentativas.'.format(3-erros))
    else:
        print('Sua senha foi bloqueada. Por favor  dirija-se a um de nossos caixas.')
        break