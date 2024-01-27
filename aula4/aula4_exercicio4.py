sal_base=float(1500)
comissao=float(200)

corretor=input('Digite o nome do(a) corretor(a): ' )
qtde_vendas=int(input('Informe a quantidade de imóveis vendidos: '))
total_vendas=float(input('Informe o valor total de vendas do(a) corretor(a): R$ '))
sal_final=sal_base+(comissao+qtde_vendas)+(total_vendas*0.05)
print('O salário final do(a) corretor(a) {} é de R${:.2f}.'.format(corretor,sal_final))