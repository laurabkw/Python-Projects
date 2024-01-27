#Exercício 1
import imp
from math import pow
def calcula_area_circulo(n1):
    calcula_area_circulo=3.14*pow(n1,2)
    return calcula_area_circulo

def calcula_area_triangulo(n1,n2):
    calcula_area_triangulo=n1*n2/2
    return calcula_area_triangulo

def calcula_area_retangulo(n1,n2):
    calcula_area_retangulo=n1*n2
    return calcula_area_retangulo

#Exercício 2
def gera_matriz_aleatoria(linhas,colunas,intervalo_inicial,intervalo_final):
    from random import randrange
    m=[[randrange(intervalo_inicial,intervalo_final) for i in range(colunas)]for j in range(linhas)]
    return m

def calcula_traco_matriz(matriz):
    traco=[]
    soma=0
    for i in range(len(matriz)):
        traco.append(matriz[i][soma])
        soma+=1
    return sum(traco)

#Exercício 3
def soma_matrizes(a,b):
    c=[]
    for i in range(a):
        c.append([])
        for j in range(len(a[i])):
            c[i].append(a[i][j]+b[a][j])
        return c

#Exercício 4
def multiplica_matriz_por_constante(matriz,constante):
    m=[]
    for i in range(len(matriz)):
        m.append([])
        for j in matriz[i]:
            m[i].append(j*constante)
        return m

#Exercício 5
def obtem_dados_dicionario():
    funcionarios=[['Ana','F'],['Beatriz','F'],['Carla','F'],['Daniela','F'],['Emílio','M'],['Fernando','M'],['Ítalo','M']]
    return funcionarios

def retorna_numero_homem_mulher(matriz):
    h=m=0
    linha=len(matriz)
    for nome,dados in matriz:
        print(nome,dados)

    for i in range(linha):
        if matriz[i][1]=='F':
            m+=1
        else:
            h+=1
    return f'\nQuantidade de mulheres cadastradas: {m} \nQuantidade de homens cadastrados: {h}'