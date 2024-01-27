frase=input('Digite uma frase ').strip().upper() #após a sopa

palavras=frase.split() #após  a  sopa
junto=''.join(palavras) #apósasopa
inverso=''

for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]

if inverso==junto:
    print('Temoa um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')