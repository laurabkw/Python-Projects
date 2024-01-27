from random import randrange

linha=int(input('Número de linhas da matriz: '))
coluna=int(input('Número de colunas da matriz: '))

lista_a=[[randrange(1,11) for i in range(coluna)] for x in range(linha)]
lista_b=[[randrange(1,11) for i in range(coluna)] for x in range(linha)]

abaixo_diagonal=0
acima_diagonal=0

for i in range(linha):
    for j in range(coluna):
        if i>j:
            abaixo_diagonal+=lista_a[i][j]
        if  i<j:
            acima_diagonal+=lista_b[i][j]

print('Matriz A:')
for i in range(linha):
    for j in range(coluna):
        print(lista_a[i][j], end=' ')
    print()

print('Matriz B:')
for i in range(linha):
    for j in range(coluna):
        print(lista_b[i][j], end=' ')
    print()

print('Soma= {}'.format(abaixo_diagonal+acima_diagonal))