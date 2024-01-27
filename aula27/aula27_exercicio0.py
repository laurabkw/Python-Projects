def escreve(msg):
    #a aspas duplas servem para criar a documentação de uma função
    ''' 
    Print de mensagem informada pelo usuário
    msg: entrada do usuário para o programa
    '''
    print('~')
    print(msg)
    print('~')

#escreve(input('Digite uma frase: '))

#help(escreve)

def teste(b):
    b+=4 #variável de espoco local
    c=2 #variável de espoco local
    print('A dentro da função vale {}.'.format(a))
    print('B dentro da função vale {}.'.format(b))
    print('C dentro da função vale {}.'.format(c))

#Programa principal
a=5 #variável de escopo global
teste(a)
print('A fora da função vale {}.'.format(a))