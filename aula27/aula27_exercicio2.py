def ficha(nome_jogador='Laura',numero_gols='99'):
    print(f'{nome_jogador}')
    print(f'{numero_gols}')

n=input('Informe o nome do jogador: ')
g=int(input('Insira o número de gols do jogador: '))

if g.isnumeric():
    g=int(g)
else:
    numero_gols=0

if n.strip()=='':
    ficha(numero_gols=g)
else:
    ficha(n,g)

if type(n)==int:
    print('Sim')
else:
    print('Não')
