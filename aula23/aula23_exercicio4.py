termo=int(input('Informe do 1º termo da PA: '))
numero_termos=int(input('Informe o número de termos da PA: '))
razao=int(input('Informe a razão da PA: '))
pa=[termo]

termo_anterior=termo

for x in range(numero_termos-1):
    termo_atual=termo_anterior+razao
    pa.append(termo_atual)
    termo_anterior=termo_atual
print(pa)

soma=sum(pa)

print('Soma dos termos da PA: {}'.format(soma))