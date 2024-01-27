atletas=[]
tempo=[]

for x in range(7):
    nome=input('Informe o nome do nadador: ')
    tempos=float(input('Informe o tempo do nadador: '))
    atletas.append(nome)
    tempo.append(tempos)

indice_melhor=tempo.index(min(tempo)) #imprime o índice do melhor tempo
indice_pior=tempo.index(max(tempo)) #imprime o índice do pior tempo

media_tempos=sum(tempo)/len(tempo)

print('O atleta {} tem o melhor tempo.'.format(atletas[indice_melhor]))
print('O atleta {} tem o pior tempo.'.format(atletas[indice_pior]))
print('Média dos tempos: {}'.format(media_tempos))