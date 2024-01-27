nome=input('Insira o nome do dono da conta bancária: ')
senha=int(input('Insira sua senha: '))
tentativas=0

for c in range (1,4):
    nome=input('Insira o nome do dono da conta bancária: ')
    senha=int(input('Insira sua senha: '))
    if senha==123456:
        print('Senha correta.\nSeja Bem-Vindo(a) {}.'.format(nome))
        break
    elif senha!=123456:
        tentativas+=1
        print('Senha Incorreta.\nVocê ainda tem {} tentativas.'.format(tentativas))
        if tentativas==3:
            print('Sua senha foi bloqueada.\nPor favor, dirija-se a um de nossos caixas.')