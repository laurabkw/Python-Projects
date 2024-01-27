mulheres=0
homens_acima=0

while True: 
    idade=int(input('Idade: '))
    if idade<0:
        break
    sexo=input('Sexo: ').upper()
    if sexo=='F':
        mulheres+=1
    elif sexo =='M' and idade>18:
        homens_acima+=1
print(f'Total de mulheres: {mulheres}\nTotal de homens acima de 18 anos: {homens_acima}')