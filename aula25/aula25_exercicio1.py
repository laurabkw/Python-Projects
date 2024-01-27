produtos=('Produto A ', 7,'Produto B ', 10,'Produto C ', 25,'Produto D ', 15,'Produto E ', 4)

for n in range(0, len(produtos)):
    if n%2==0:
        print(produtos[n], end='')
    else:
        print(produtos[n])