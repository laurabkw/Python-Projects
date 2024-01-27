altura1=float(input('Digite aqui a altura da primeira pessoa: '))
altura2=float(input('Digite aqui a altura da segunda pessoa: '))
altura3=float(input('Digite aqui a altura da terceira pessoa: '))

alturas = [altura1, altura2, altura3]
alturas.sort(reverse = True)
print('A ordem das alturas do mais alto ao mais baixo é {}, {}, {}.'.format(alturas[0],alturas[1],alturas[2]))