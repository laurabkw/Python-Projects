lista=[12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]
maior_valor=lista[0]
menor_valor=lista[0]
lista_pares=[]
ocorrencia=0
media_elementos=0
soma_negativo=0

for index in range(0,len(lista)):
    #maior valor
    if maior_valor<lista[index]:
        maior_valor=lista[index]

    #menor valor
    if menor_valor>lista[index]:
        menor_valor=lista[index]

    #lista de números pares
    if lista[index]%2==0:
        lista_pares.append(lista[index]) #lista_pares=[12,....(outros números de resto 2)]

    #ocorrência do primeiro elemento da lista (neste caso 12)
    if lista[index]==lista[0]:
        ocorrencia+=1

    #somatório para média
    media_elementos+=lista[index]

    #soma dos números negativos
    if lista[index]<0:
        soma_negativo+=lista[index]

#média
media_elementos/=len(lista)

print(lista)
print('Maior elemento da lista: {}'.format(maior_valor))
print('Menor elemento da lista: {}'.format(menor_valor))
print('Lista de números pares: {}'.format(lista_pares))
print('Número de ocorrências do primeiro elemento da lista: {}'.format(ocorrencia))
print('Média dos elementos da lista: {}'.format(media_elementos))
print('Soma dos elementos negativos da lista: {}'.format(soma_negativo))