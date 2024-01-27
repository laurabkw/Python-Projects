valor=int(input('Insira o valor que deseja sacar: '))
total=valor
cedula=50
total_cedulas=0
while True:
    if total >= cedula:
        total-=cedula
        total_cedulas+=1
    else:
        if total_cedulas>0:
            print('Total de {} cédulas de R$ {}'.format(total_cedulas,cedula))
        if cedula==50:
            cedula=20
        elif cedula==20:
            cedula=10
        elif cedula==10:
            cedula=1
        total_cedulas=0
        if total==0:
            break
