aprovado    = 0
prova_final = 0
reprovado   = 0
 
num_alunos = 5
for i in range(num_alunos):
   N1 = float(input('\nNota 1: '))
   N2 = float(input('Nota 2: '))
   media = (N1 + N2) / 2
   
   if media >= 6:
      aprovado += 1
   elif media < 2:
      reprovado += 1
   else:
      prova_final += 1
                         
print('\nAprovados..: {:.2f}'.format((aprovado / num_alunos) * 100))
print('Prova final: {:.2f}'.format((prova_final / num_alunos) * 100))
print('Reprovados.: {:.2f}'.format(((reprovado / num_alunos) * 100)))