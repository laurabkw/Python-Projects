#Exercício 1
def somaImposto(taxaImposto,custo_produto):
    taxa=(taxaImposto/100)*custo_produto
    custo_produto+=taxa
    return custo_produto

#Exercício 2


#Exercício 3
def valorPagamento(valor_prestacao,dias_atraso):
    total=(dias_atraso*0.1+3.0)+valor_prestacao
    return total

#Exercício 4

def digitosNumero(n):
    digitos=len(str(n))
    return digitos

#Exercício 5
#def numeroReverso(n):
    #reverso=reverse(str(n))
    #return reverso