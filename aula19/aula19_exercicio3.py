resposta='S'
soma=quantidade=media=maior=menor=0

while resposta in 'S':
    numero=int(input('Digite aqui um número: '))
    soma+=numero
    quantidade+=1
    if quantidade==1:
        maior=menor=numero
    else:
        if numero>maior:
            maior=numero
        if numero<menor:
            menor=numero
    resposta=input('Quer continuar [S/N]? ').upper().strip()
media=soma/quantidade

print('Você digitou {} números e a média entre eles foi {}.'.format(quantidade,media))
print('O maior valor digitado foi {} e o menor valor digitado foi {}.'.format(maior,menor))