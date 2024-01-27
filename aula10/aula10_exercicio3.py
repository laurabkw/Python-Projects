peso=float(input('Digite aqui seu peso: '))
altura=float(input('Digite aqui sua altura: '))
imc=peso/(altura**2)
print('O seu IMC é de {:.1f}'.format(imc))

if imc<18.5:
    print('Você está abaixo do peso ideal.')
elif 18.5 <= imc < 25:
    print('Você está com peso normal.')
elif 25 <= imc < 30:
    print('Você está em sobrepeso.')
elif 30 <= imc < 40:
    print('Você está em obesidade.')
elif imc >= 40:
    print('Você está com obesidade mórbida.')