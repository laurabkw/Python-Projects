copo1='laranja'
copo2='acerola'

print('Antes da troca: \nCopo 1 tem {} \nCopo2 tem {}.'.format(copo1,copo2))
copo1, copo2, = copo2, copo1
print('Depois da troca: \nCopo 1 tem {} \nCopo2 tem {}.'.format(copo1,copo2))