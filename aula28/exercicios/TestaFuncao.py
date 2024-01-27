from MinhasFuncoes import *

'''Exercício 1
escolha=int(input('Escolha a figura que você deseja calcular a área: \n1.Círculo \n2.Triângulo \n3.Retângulo '))
if escolha==1:
    numero1=int(input('Digite o primero número: ')) #Variáveis usadas no exercício 1
    c=calcula_area_circulo(numero1)
    print('A área do círculo é {}.'.format(c))
else:
    numero1=int(input('Digite o primero número: ')) #Variáveis usadas no exercício 1
    numero2=int(input('Digite o segundo número: ')) #Variáveis usadas no exercício 1
    if escolha<0 or escolha>3:
        print('Opção Invalida.')
    elif escolha==1:
        c=calcula_area_circulo(numero1)
        print('A área do círculo é {}.'.format(c))
    elif escolha==2:
        t=calcula_area_triangulo(numero1,numero2)
        print('A área do triângulo é {}.'.format(t))
    elif escolha==3:
        r=calcula_area_retangulo(numero1,numero2)
        print('A área do retângulo é {}.'.format(r))'''


linhas=int(input('Digite a quantidade de linhas da matriz: ')) #Variáveis usadas nos exercícios 2 e 3
colunas=int(input('Digite a quantidade de colunas da matriz: ')) #Variáveis usadas nos exercícios 2 e 3
intervalo_inicial=int(input('Digite o intervalo inicial da matriz: ')) #Variáveis usadas nos exercícios 2 e 3
intervalo_final=int(input('Digite o intervalo final da matriz: ')) #Variáveis usadas nos exercícios 2 e 3

''' Exercício 2
m=gera_matriz_aleatoria(linhas,colunas,intervalo_inicial,intervalo_final)
print('Matriz gerada: {}'.format(m))

if len(m)==len(m[0]):
    print('O traço da matriz gerada: {}'.format(calcula_traco_matriz))
else:
    print('Não foi possível calcular o traço pois a matriz não é quadrada.')'''

''' Exercício 3
a=gera_matriz_aleatoria(linhas,colunas,intervalo_inicial,intervalo_final) #Variáveis usadas no exercício 2 e 3
b=gera_matriz_aleatoria(linhas,colunas,intervalo_inicial,intervalo_final) #Variáveis usadas no exercício 2 e 3

if len(a)==len(b) and len(a[0]==len(b[0])):
    print('Matriz A: {}\nMatriz B: {}\nMatriz C: {}.'.format(a,b,soma_matrizes(a,b)))
else:
    print('As matrizes não tem a mesma ordem.')'''

''' Exercício 4
m1=gera_matriz_aleatoria(linhas,colunas,intervalo_inicial,intervalo_final)
constante=int(input('Digite o constante da matriz: '))
print('Matriz gerada: {}\nMatriz C (M1 * Constante)= {}'.format(m1,multiplica_matriz_por_constante(m1,constante)))'''

'''Exercício 5
cadastro=obtem_dados_dicionario()
print(retorna_numero_homem_mulher(cadastro))'''