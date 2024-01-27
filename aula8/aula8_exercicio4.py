from random import choice

aluno1=input('Escrava o nome do primeiro aluno: ')
aluno2=input('Escrava o nome do segundo aluno: ')
aluno3=input('Escrava o nome do terceiro aluno: ')
aluno4=input('Escrava o nome do quarto aluno: ')
alunos=[aluno1,aluno2,aluno3,aluno4]

aluno_escolhido=choice(alunos)
print('O aluno escolhido foi {}.'.format(aluno_escolhido))