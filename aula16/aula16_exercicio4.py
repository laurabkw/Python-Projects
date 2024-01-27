soma=0
nome=input('Nadador 1: ')
tempo=float(input('Tempo do nadador 1: '))

melhor_nadador=nome
melhor_tempo=tempo
pior_nadador=nome
pior_tempo=tempo

soma_tempo=0

soma+=tempo
tempo12s15s=0

if 12<= tempo <= 15:
    tempo12s15s+=1

for nadador in range (2,8):
    nome=input(f'Nadador {nadador}: ')
    tempo=float(input(f'Tempo do nadador {nadador}: '))

    if tempo<melhor_tempo:
        melhor_nadador=nome
        melhor_tempo=tempo
    elif tempo>pior_tempo:
        pior_nadador=nome
        pior_tempo=tempo
    
    soma_tempo+=1

    if 12<= tempo <= 15:
        tempo12s15s+=1

print(f'{melhor_nadador} é o melhor nadador com {melhor_tempo} segundos. \n{pior_nadador} é o pior nadador com {pior_tempo} segundos')

media=soma_tempo/7

print(f'Média dos tempos: {media:.2f} segundos.\nAtletas entre  12 e 15 segundos: {tempo12s15s}')