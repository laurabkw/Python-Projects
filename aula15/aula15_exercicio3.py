soma_idade=0
maior_idade_homem=0
nome_mais_velho=''
mulher_menor=0
media_idade=0

for p in range(1,5):
    nome=input('Nome: ').strip()
    idade=int(input('Idade: '))
    sexo=input('Sexo [F/M]: ').strip().upper()
    soma_idade+=idade

    if p==1 and sexo in 'M':
        maior_idade_homem=idade
        nome_mais_velho=nome

    if sexo in 'M' and idade>maior_idade_homem:
        maior_idade=idade
        nome_mais_velho=nome
    
    if sexo in 'F' and idade<20:
        mulher_menor+=1
media_idade=soma_idade/4

print('A média de idade do grupo é de {} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem,nome_mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulher_menor))