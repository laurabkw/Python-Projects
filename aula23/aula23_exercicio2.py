linha=int(input('Número de linhas da matriz: '))
coluna=int(input('Número de colunas da matriz: '))

if linha!=coluna:
    print('Matriz não triangular.')
else:
    m=[]
    triangular=True
    for i in range(linha):
        elemento=[]
        for j in range(coluna):
            elemento.append(int(input('M[{}][{}] = '.format(i+1,j+1))))
        m.append(elemento)
        
    print('Matriz M')
    for i in range(linha):
        for j in range(coluna):
            print(m[i][j],end=' ')
        print()

    for i in range(linha):
        for j in range(coluna):
            if i<j:
                if m[i][j]!=0:
                    triangular=False
                    break
    if triangular==True:
        print('A matriz M é uma matriz triangular inferior.')
    else:
        print('A matriz M não é uma matriz triangular inferior.')