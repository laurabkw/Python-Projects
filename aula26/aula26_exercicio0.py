def exibirMensagem(): #Declarando uma função
    print('Python é fácil')

# Programa principal
exibirMensagem() # Chamando a execução da função

def exibirMensagemBoasVindas(pessoa, mensagem): # Função com passagem de parâmetro
    print('{}, {}'.format(mensagem,pessoa))

exibirMensagemBoasVindas('Janaína', 'Boas-Vindas')

exibirMensagemBoasVindas()

def exibirMensagemBoasVindas(pessoa='Fulano', mensagem='Bem-Vindo'):
    print('{}, {}'.format(mensagem,pessoa))

exibirMensagemBoasVindas()