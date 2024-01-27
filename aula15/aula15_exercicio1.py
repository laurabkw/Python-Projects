from datetime import date

atual=date.today().year
total_maior=0
total_menor=0

for pessoa in range(1,8):
    nascimento=int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    idade=atual-nascimento
    if idade >=21:
        total_maior+=1
    else:
        total_menor+=1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(total_maior))
print('E também tivemos {} pessoas menores de idade.'.format(total_menor))