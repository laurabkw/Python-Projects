lista=['Maria','Janaína','José','Carlos']
lista_a=['José','Pedro']

#for n in range(0,len(lista)):
#lista.append('Jorge')
#lista.insert(0,'Jorge')
#lista.sort(reverse=True)
#del lista[-1] - deletar um valor da lista localizado no vetor específico, no exemplo, o valor localizado na posição 0
#lista.remove('Janaína') - deletar um valor da lista correspondente ao digitado, no exemplo, 'Janaína'
#lista.pop()
#lista.clear() - limpar a lista
#lista_a=lista
#lista_a=lista[:]
#lista.append('José')
#print(lista.index('Janaína'))
#lista.extend(lista_a)

'''for indice, nome in enumerate(lista):
    print('{} está armazenado no índice {}'.format(nome,indice))'''

a=[[2,1,-5],[3,7,0],[6,4,8]]
#print(a[0][0],a[0][1],a[0][2])

soma_a=0
lin=len(a)
col=len(a[0])

for i in range(lin):
    for j in range(col):
        soma_a+=a[i][j]

print(soma_a)