palavras=['teclado', 'celular', 'cadeira', 'mesa', 'trabalho', 'pesquisar']

for j in palavras:
    vogais=[i for i in j if i in ['a', 'e', 'i', 'o', 'u']]
    print(vogais)